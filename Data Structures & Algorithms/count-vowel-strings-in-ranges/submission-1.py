class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def goodv(self, string):
            vowels = ['a','e','i','o','u']
            if string[0] in vowels and string[-1] in vowels:
                return True
            else:
                return False
        res = list()
        for indexes in queries:
            count = 0
            for i in range(indexes[0],indexes[1]+1):
                if goodv(self,words[i]):
                    count +=1
            res.append(count)
        return res
                
            