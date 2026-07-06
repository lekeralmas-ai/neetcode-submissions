class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            left_sum = 0
            right_sum = 0
            for a in range(i):
                left_sum += nums[a]
            for j in range(i+1,len(nums)):
                right_sum += nums[j]
            if right_sum == left_sum:
                return i
        return res