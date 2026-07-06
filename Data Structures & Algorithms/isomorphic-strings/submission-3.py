class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            diff = ord(s[i]) - ord(t[i])
            if s[i] not in s_map:
                s_map[s[i]] = diff
            if t[i] not in t_map:
                t_map[t[i]] = diff
            if diff != s_map[s[i]] or diff != t_map[t[i]]:
                return False
        return True