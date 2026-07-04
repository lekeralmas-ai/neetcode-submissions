class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        res = {}      
        used = set()      
        for i in range(len(s)):
            if s[i] not in res:
                if t[i] in used:          
                    return False
                res[s[i]] = ord(s[i]) - ord(t[i])   
                used.add(t[i])
            else:
                if res[s[i]] != ord(s[i]) - ord(t[i]):
                    return False
        return True