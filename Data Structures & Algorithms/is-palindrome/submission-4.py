class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1, s2 = 0, len(s) -1 
        while s1 < s2:
            while s1 < s2 and not self.is_al(s[s1]):
                s1 +=1
            while s2 > s1 and not self.is_al(s[s2]):
                s2 -=1
            if s[s1].lower() != s[s2].lower():
                return False
            s1 += 1
            s2 -=1
        return True



    def is_al(self, ch):
        return ('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9')
