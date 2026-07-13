class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        nums.sort(key= lambda n:(d[n],-n))
        return nums
