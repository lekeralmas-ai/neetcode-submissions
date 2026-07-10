class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        res = list()
        for key,value in d1.items():
            if key in d2:
                res.append(key)
        return res