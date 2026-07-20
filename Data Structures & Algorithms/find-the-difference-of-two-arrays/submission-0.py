class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d = set(nums1+nums2)
        res1 = []
        res2 = []
        for i in d:
            if i not in nums2:
                res1.append(i)
            elif i in nums1 and nums2:
                continue
            else:
                res2.append(i)
        return [res1,res2]
