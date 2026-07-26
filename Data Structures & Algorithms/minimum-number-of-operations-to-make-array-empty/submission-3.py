class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        d = Counter(nums)
        
        for freq in d.values():
            if freq == 1:
                return -1
            if freq % 3 == 0:
                res += freq // 3
            elif freq % 3 == 1:
                res += (freq // 3) - 1 + 2
            else: 
                res += (freq // 3) + 1      
        return res