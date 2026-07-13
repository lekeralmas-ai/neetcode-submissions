class Solution:
    def specialArray(self, nums: List[int]) -> int:
        d = Counter(nums)
        for i in range(max(nums)+1):
            s = 0
            for num in d:
                if num >= i:
                    s +=  d[num]
            if s == i:
                return i
        return -1