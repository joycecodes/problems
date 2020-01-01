import collections

graph ={"Panda": ["Towel", "Sand"],
 "Sand": ["Case", "Bottle"],
"Case": ["Death", "Medicine"],
 "Medicine": ["Shirt", "Doodle"]
 }
start = "Panda"
end = "Doodle"


def path(graph, start, end):
    q = collections.deque()
    visited = set()
    q.append([start, 0])

    while len(q) > 0:
        n, level = q.popleft()
        visited.add(n)
        if n == end:
            return level
        if n in graph:
            for key in graph[n]:
                if key not in visited:
                    q.append([key, level + 1])
    return -1

print(path(graph, start, end))
