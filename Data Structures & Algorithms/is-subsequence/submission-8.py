class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        if not s:
            return True
        for i in range(len(t)):
            if l < len(s) and s[l] == t[i]:
                l += 1
        return l == len(s)