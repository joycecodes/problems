"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        h = {}
        for course in prerequisites:
            end, start = course
            h[start] = h.get(start, []) + [end]
        for key in h:
            if h[key]:
                q = []
                visiting = set()
                visited = set()
                q.append(key)
                print(key)
                while q:
                    n = q[-1]
                    visiting.add(n)
                    if n in h and h[n]:
                        temp = h[n].pop()
                        if temp not in visiting:
                            q.append(temp)
                        else:
                            return False
                    else:
                        q.pop()
                        visited.add(n)
                        visiting.remove(n)
        return True