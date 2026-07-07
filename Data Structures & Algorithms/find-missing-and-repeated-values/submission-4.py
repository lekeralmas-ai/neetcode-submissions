class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) 
        d = defaultdict(int)
        for i in range(n):
            for j in range(n):
                d[grid[i][j]] += 1
        miss = double = 0
        for i in range(1,n**2 +1):
            if d[i] == 2:
                double = i
            if d[i] == 0:
                miss = i
        return [double, miss]