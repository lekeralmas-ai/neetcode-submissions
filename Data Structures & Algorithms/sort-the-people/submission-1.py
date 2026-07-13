class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        for h,n in zip(heights, names):
            d[h] = n
        res = list()
        for j in sorted(heights,reverse = True):
            res.append(d[j])
        return res