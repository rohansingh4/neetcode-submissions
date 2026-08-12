class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while lo <= hi:
            mid  = (lo + hi) // 2
            hours = 0
            for pile in piles:
                hours += ((pile+mid -1)// mid)
            if hours  <= h:
                hi = mid -1
            else:
                lo = mid + 1
        return lo