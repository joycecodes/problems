"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s)
from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
"""

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        h = {}
        for word in wordList:
            for i in range(len(word)):
                temp = word[:i] + "*" + word[i + 1:]
                h[temp] = h.get(temp, []) + [word]

        max_len = len(wordList) + 1
        queue = collections.deque()
        visited = set([])

        for i in range(len(beginWord)):
            if (beginWord[:i] + '*' + beginWord[i + 1:]) in h:
                for w in h[beginWord[:i] + '*' + beginWord[i + 1:]]:
                    queue.append([w, [beginWord], 1])
                    visited.add(beginWord)
        res = []
        while queue:
            w, old_path, length = queue.popleft()
            path = old_path[:]
            path.append(w)
            visited.add(w)
            length += 1
            if length > max_len:
                continue
            if w == endWord:
                if length < max_len:
                    max_len = length
                res.append(path)

            for i in range(len(beginWord)):
                if w[:i] + '*' + w[i + 1:] in h:
                    for next_w in h[w[:i] + '*' + w[i + 1:]]:
                        if next_w not in path and next_w not in visited:
                            queue.append((next_w, path, length))
        return res