class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cin = Counter(words[0])
        for word in words:
            cur = Counter(word)
            for c in cin:
                cin[c] = min(cin[c], cur[c])
        res = []
        for c in cin:
            for j in range(cin[c]):
                res.append(c)
        return res