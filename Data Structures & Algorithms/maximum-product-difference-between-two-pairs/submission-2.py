class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        n = sorted(nums)
        l = len(nums)
        return n[l-1]*n[l-2]-n[0]*n[1]