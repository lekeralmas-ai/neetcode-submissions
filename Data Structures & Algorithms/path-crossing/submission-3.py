class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dir = {
            'N' : [1,0],
            'S' : [-1,0],
            'E' : [0,1],
            'W' : [0,-1]
        }
        seen = set()
        x,y = 0,0
        seen.add((x,y))
        for i in path:
            dx,dy = dir[i]
            x,y = x+dx, y+ dy
            if (x,y) in seen:
                return True
            else:
                seen.add((x,y))
        return False
