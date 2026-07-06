class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = list()
        for i in range(len(nums1)):
            greater = -1 
            k = 0
            while k < len(nums2) and nums2[k] != nums1[i]:
                k += 1
            for j in range(k + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    greater = nums2[j]
                    break 
                    
            res.append(greater)
        return res