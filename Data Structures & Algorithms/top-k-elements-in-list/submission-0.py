class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        sorted_frequency = sorted(frequency.items(), key=lambda item:item[1], reverse = True)
        result = []
        for num, freq in sorted_frequency[:k]:
            result.append(num)
        
        return result