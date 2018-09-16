def scc(graph, n):
    cnt = 1
    node_cnt = 0
    components = {}
    sinks = find_sink(graph, n)
    for sink in sinks:
        components[cnt] = 1
        cnt += 1
        node_cnt += 1
        relax_edges(graph, sink)

    while node_cnt != n and len(graph) > 0:
        start = next(iter(graph))
        cycle = find_cycle(start, graph)
        components[cnt] = len(cycle)
        cnt += 1
        node_cnt += len(cycle)
        for cycle_node in cycle:
            graph.pop(cycle_node)
            relax_edges(graph, cycle_node)
        print(cycle)

    print(components)


def find_cycle(start, graph):
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


def relax_edges(graph, v):
    for node in graph:
        if v in graph[node]:
            graph[node].pop(v)


def find_sink(graph, n):
    sinks = []
    for i in range(1, n + 1):
        if i not in graph:
            sinks.append(i)
    return sinks


file = open("input.txt", "r")
n, m = map(int, file.readline().split())

graph = {}
for i in range(0, m):
    u, v = map(int, file.readline().split())
    if u in graph:
        graph[u][v] = 0
    else:
        graph[u] = {v: 0}

file.close()

print(graph)
scc(graph, n)
