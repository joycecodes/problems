"""
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every
letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter,
and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern.

You may return the answer in any order.

"""
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            h1 = {}
            h2 = {}
            match = True

            for i in range(len(word)):
                if word[i] not in h1:
                    h1[word[i]] = pattern[i]
                elif h1[word[i]] != pattern[i]:
                    match = False
                    break

                if pattern[i] not in h2:
                    h2[pattern[i]] = word[i]
                elif h2[pattern[i]] != word[i]:
                    match = False
                    break
            if match:
                res.append(word)

        return res