class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if nums == sorted(nums):
            return True
        for i in range(1,n):
            new_rotation = [0]*n
            for j in range(n):
                new_rotation[j] = nums[(i+j)%len(nums)]
            if sorted(nums) == new_rotation:
                return True
        return False