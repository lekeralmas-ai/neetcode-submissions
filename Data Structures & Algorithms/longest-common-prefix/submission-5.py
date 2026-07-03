class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mock = strs[0]
        lmin = len(strs[0])
        for st in strs:
            curr_l = 0
            while curr_l < len(st) and curr_l < len(mock) and st[curr_l] == mock[curr_l]:
                curr_l += 1
            lmin = min(curr_l, lmin)
        return mock[:lmin]
            