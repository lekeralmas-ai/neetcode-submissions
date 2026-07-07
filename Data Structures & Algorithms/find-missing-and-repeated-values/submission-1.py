class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = list()
        a = 0
        b = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in res:
                    a = grid[i][j]
                else:
                    res.append(grid[i][j])
        for i in range(1,len(grid)**2+1):
            if i not in res:
                b = i
        return [a,b]
