class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        res = list()
        for num in arr2:
            while c[num] != 0:
                res.append(num)
                c[num] -=1
        res2 = list()
        for i in arr1:
            if i not in arr2:
                res2.append(i)
        res += sorted(res2)
        return res