class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = defaultdict(int)
        for word in words:
            for j in range(len(word)):
                d[word[j]] +=1
        for key,value in d.items():
            if value % len(words) != 0:
                return False
        return True