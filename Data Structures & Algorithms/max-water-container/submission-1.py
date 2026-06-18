class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 1
        if len(heights) == 2:
            return min(heights[0],heights[1]) 
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if min(heights[i],heights[j]) * (j-i) > area:
                    area = min(heights[i],heights[j]) * (j-i)
        return area