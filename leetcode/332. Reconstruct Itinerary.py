"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK.
Thus, the itinerary must begin with JFK.
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        h = {}
        for ticket in tickets:
            start, end = ticket
            h[start] = h.get(start, []) + [end]

        for key in h:
            h[key].sort(reverse=True)

        stack = ["JFK"]
        res = []

        while stack:
            n = stack[-1]
            if n in h and h[n]:
                stack.append(h[n].pop())
            else:
                res.append(stack.pop())

        return res[::-1]