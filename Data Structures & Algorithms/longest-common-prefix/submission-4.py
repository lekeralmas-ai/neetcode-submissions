class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mock = strs[0]
        ll = list()
        for st in strs:
            curr_l = 0
            while curr_l < len(st) and curr_l < len(mock) and st[curr_l] == mock[curr_l]:
                curr_l += 1
            ll.append(curr_l)
        return mock[:min(ll)]
            