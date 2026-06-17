class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(len(nums)):
            suum = 1
            for j in range(i + 1, len(nums)):
                suum *= nums[j]
            for k in range(i):
                suum *= nums[k]
            result[i] = suum
        return result