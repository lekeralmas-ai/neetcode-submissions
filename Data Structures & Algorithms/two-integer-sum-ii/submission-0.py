class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nel= list()
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    nel.append(i+1)
                    nel.append(j+1)
                    return nel