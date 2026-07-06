class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        res = 0
        for num in nums:
            d[num] = d.get(num,0) + 1
        for num, freq in d.items():
            if freq > len(nums)/2:
                res = num
        return res