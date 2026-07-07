class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) 
        seen = set()
        missing = double = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] in seen:
                    double = grid[i][j]
                seen.add(grid[i][j])
        for i in range(1,n*n+1):
            if i not in seen:
                missing = i
                break
        return [double,missing]
