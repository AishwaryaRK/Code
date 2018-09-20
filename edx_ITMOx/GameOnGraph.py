def get_winner(graph, s):
    visited = {}
    stack = [s]
    leaf_distances = []
    distance = 0
    while stack != []:
        node = stack.pop()
        visited[node] = True
        if node != s:
            distance += 1
        if node in graph:
            for neighbor in graph[node]:
                stack.append(neighbor)
        else:
            leaf_distances.append(distance)
            distance -= 1

    return "Alice" if any(d % 2 != 0 for d in leaf_distances) else "Bob"


file = open("input.txt", "r")
n, m, s = map(int, file.readline().split())

graph = {}
for i in range(0, m):
    u, v = map(int, file.readline().split())
    if u in graph:
        graph[u][v] = True
    else:
        graph[u] = {v: True}

file.close()

winner = get_winner(graph, s)

file = open("output.txt", "w")
file.write(winner)
file.close()
