class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        dblnums = nums + nums
        count = 1
        for i in range(1, 2*n):
            if dblnums[i-1] <= dblnums [i]:
                count += 1
            else:
                count = 1
            if count == n:
                return True
        return False