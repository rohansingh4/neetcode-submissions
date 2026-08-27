class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []
        left = right = 0
        while right < len(nums):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            
            dq.append(right)

            if dq and dq[0] < left:
                dq.popleft()
            
            if right + 1 >= k:
                result.append(nums[dq[0]])
                left += 1
            right += 1
        return result 