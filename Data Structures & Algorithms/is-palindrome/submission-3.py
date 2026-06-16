class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_n = s.lower()
        s_n1 = list()
        for i in range(len(s)):
            if 'a' <= s_n[i] <= 'z' or '0'<=s_n[i]<='9':
                s_n1.append(s_n[i])
        for i in range(len(s_n1)):
            if s_n1[i] != s_n1[len(s_n1)-1-i]:
                return False
        return True