class Solution:
    def maxDifference(self, s: str) -> int:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        maxf=0
        minf= len(s)
        for letter, freq in d.items():
            if freq % 2 == 1:
                maxf = max(maxf,freq)
            else:
                minf = min(minf,freq)
        return maxf-minf