class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = Counter(chars)
        res = 0
        for i in words:
            timed = Counter(i)
            good = True
            for key, value in timed.items():
                if value > d[key]:
                    good = False
                    break
            if good:
                res += len(i)
        return res