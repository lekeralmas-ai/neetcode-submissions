class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def is_substring(word1, word2):
            for i in range(len(word2)):
                current_l = 0
                for j in range(len(word1)):
                    if i + j < len(word2) and word1[j] == word2[i+j]:
                        current_l += 1
                    else:
                        break
                if current_l == len(word1):
                    return True
            return False

        res = list()
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and is_substring(words[i], words[j]):
                    res.append(words[i])
                    break
        return res