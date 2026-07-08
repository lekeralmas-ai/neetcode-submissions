class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        d1 = defaultdict(str)
        d2 = defaultdict(str)
        if len(s) != len(pattern):
            return False
        for st in range(len(pattern)):
            if pattern[st] not in d1:
                d1[pattern[st]] = s[st]
            else:
                if d1[pattern[st]] != s[st]:
                    return False
        for st in range(len(pattern)):
            if s[st] not in d2:
                d2[s[st]] = pattern[st]
            else:
                if d2[s[st]] != pattern[st]:
                    return False
        return True