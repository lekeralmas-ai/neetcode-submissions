class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        res =[]
        for key,value in d.items():
            if value > len(nums) / 3:
                res.append(key)
        return res