class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l_new = list()
        for i in range(len(nums)*2):
            if i > len(nums) -1:
                l_new.append(nums[i-len(nums)])
            else:
                l_new.append(nums[i])
        return l_new