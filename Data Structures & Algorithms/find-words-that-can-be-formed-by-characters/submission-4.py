class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = Counter(chars)
        res = 0
        for i in words:
            d2 = Counter(i)
            good = True
            for c in d2:
                if  d2[c] > d[c]:
                    good = False
                    break
            if good:
                res += len(i)
        return res