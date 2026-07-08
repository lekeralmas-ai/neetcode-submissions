class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        '''d= defaultdict(int)
        count =0
        for i in nums:
            d[i] += 1
        for keys,value in d.items():
            if value > 2:
                count += value
            if value == 2:
                count += 1
        return count'''
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    count += 1
        return count
