class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        for key,value in d.items():
            if d[key] %2 != 0:
                return False
        return True