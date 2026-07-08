class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d= defaultdict(int)
        lar = -1
        for i in arr:
            d[i] += 1
        for i,vals in d.items():
            if i == d[i]:
                lar = max(lar,i)
        return lar