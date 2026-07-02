class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_l = list()
        for i in range (len(arr)-1):
            max_r = arr[i+1]
            for j in range(i+1, len(arr)):
                max_r = max(max_r, arr[j])
            new_l.append(max_r)
        new_l.append(-1)
        return new_l