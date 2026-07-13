class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a','e','i','o','u']
        res = list()
        for indexes in queries:
            count = 0
            for i in range(indexes[0],indexes[1]+1):
                if words[i][0] in vowels and words[i][-1] in vowels:
                    count +=1
            res.append(count)
        return res
                
            