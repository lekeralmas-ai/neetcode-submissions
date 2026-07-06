class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res= 0 
        for i in range(len(nums)):
            currentsum = 0
            j = i
            while j < len(nums) -1 and nums[j+1] > nums[j]:
                currentsum += nums[j]
                j += 1
            currentsum += nums[j]
            res = max(res, currentsum)
        return res