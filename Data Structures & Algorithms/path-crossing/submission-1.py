class Solution:
    def isPathCrossing(self, path: str) -> bool:
        position = list()
        x,y = 0,0
        position.append([x,y])
        for i in path:
            if i == "N":
                x +=1
            elif i == "S":
                x -=1
            elif i == "W":
                y -=1
            else:
                y +=1
            if [x,y] in position:
                return True
            else:
                position.append([x,y])
        return False