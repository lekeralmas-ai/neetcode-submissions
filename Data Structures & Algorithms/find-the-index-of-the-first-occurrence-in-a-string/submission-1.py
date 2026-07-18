class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        for i in range(len(haystack) - len(needle) + 1):
            curned = haystack[i:i+len(needle)]
            if curned == needle:
                return i
        return res