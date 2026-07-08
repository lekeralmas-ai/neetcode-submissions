class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = Counter(nums)
        count = 0 
        for keys,value in d.items():
            count += value*(value-1) //2
        return count