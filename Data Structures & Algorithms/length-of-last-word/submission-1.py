class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        while s[i] == ' ':
            i -=1
        t = i
        while s[t] != ' ' and t >=0:
            t -=1
        return i-t