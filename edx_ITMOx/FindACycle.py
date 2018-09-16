# def get_cycle_start_node(start, graph):
#     visited = {}
#     stack = [start]
#     while stack != []:
#         node = stack.pop()
#         visited[node] = True
#         if node in graph:
#             for neighbor in graph[node]:
#                 if neighbor in visited:
#                     return neighbor
#                 stack.append(neighbor)
#
#     return None


def get_cycle_nodes(start, graph):
    visited = {}
    stack = [start]
    cycle = []
    while stack != []:
        node = stack.pop()
        visited[node] = True
        cycle.append(node)
        if node in graph:
            for neighbor in graph[node]:
                if neighbor in visited:
                    index = cycle.index(neighbor)
                    return cycle[index:]
                stack.append(neighbor)
        else:
            cycle.pop()
    return None


file = open("input.txt", "r")
n, m = map(int, file.readline().split())

graph = {}
start = None
for i in range(0, m):
    u, v = map(int, file.readline().split())
    if start == None:
        start = u
    if u != v:
        if u in graph:
            value = graph[u]
            value[v] = True
            graph[u] = value
        else:
            graph[u] = {v: True}
file.close()

cycle = get_cycle_nodes(start, graph)
file = open("output.txt", "w")
if cycle == None:
    file.write("NO")
else:
    file.write("YES\n")
    cycle.reverse()
    c = ' '.join(str(e) for e in cycle)
    file.write(c)
file.close()
