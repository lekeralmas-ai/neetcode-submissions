class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = list()
        res.append(1)
        for i in range(len(nums)):
            current = i
            if current < len(nums) - 1 and nums[current + 1] > nums[current]:
                while current < len(nums)-1 and nums[current+1] > nums[current]:
                    current += 1
                res.append(current - i + 1)
            elif current < len(nums) - 1 and nums[current + 1] < nums[current]:
                while current < len(nums)-1 and nums[current+1] < nums[current]:
                    current += 1
                res.append(current - i + 1)
        return max(res)