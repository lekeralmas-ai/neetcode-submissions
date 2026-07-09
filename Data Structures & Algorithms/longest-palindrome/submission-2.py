from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        
        res = 0
        has_odd = False
        for value in d.values():
            res += (value // 2) * 2
            if value % 2 == 1:
                has_odd = True
        if has_odd:
            res += 1
            
        return res