class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            good = True
            for st in word:
                if st not in allowed:
                    good = False
                    break
            if good:
                count +=1
        return count