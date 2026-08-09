class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product = []
        # multiplier = 1
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             multiplier *= nums[j]
        #     product.append(multiplier)
        #     multiplier = 1
        # return product
        product = []
        prefix = 1
        for i in range(len(nums)):
            product.append(prefix)
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums)- 1, -1, -1):
            product[i] *= suffix
            suffix *= nums[i]
        return product