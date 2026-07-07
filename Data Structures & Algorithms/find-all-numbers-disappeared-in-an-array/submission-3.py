class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d= {}
        res = list()
        for i in nums:
            if i not in d:
                d[i] = 0
            else:
                d[i] +=1 
        for i in range(1,len(nums)+1):
            if i not in d:
                res.append(i)
        return res