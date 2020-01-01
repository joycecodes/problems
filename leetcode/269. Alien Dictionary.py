"""
There is a new alien language which uses the latin alphabet.
However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary,
where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.
"""
class Solution(object):
    def alienOrder(self, words):
        def addEdge(word1, word2):
            i = 0
            while i < len(word1) and i < len(word2):
                char1 = word1[i]
                char2 = word2[i]
                if char1 != char2:
                    if char2 not in graph[char1]:
                        graph[char1].append(char2)
                    break
                i += 1

        graph = {}
        visited = set([])
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = []
        # print(graph)
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            addEdge(word1, word2)

        # Check if graph is acyclic
        for ch in graph:
            if graph[ch]:
                stack = [ch]
                visiting = set()
                visited = set()
                while stack:
                    n = stack.pop()
                    visiting.add(n)
                    if n in graph and graph[n]:
                        for neigh in graph[n]:
                            if neigh not in visiting:
                                stack.append(neigh)
                                visiting.add(neigh)
                            else:
                                return ""
                    else:
                        visited.add(n)
                        visiting.remove(n)

        # topological sort
        visited = set()
        ans = []
        for w in graph:
            stack = [w]
            while stack and w not in ans:
                n = stack[-1]
                if n in graph and n not in visited:
                    visited.add(n)
                    for neigh in graph[n]:
                        if neigh not in visited:
                            stack.append(neigh)
                else:
                    ans.append(stack.pop())
            # visited.clear()
        return "".join(ans[::-1])