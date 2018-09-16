#Incorrect

def weight_edges(graph, m):
    nodes_with_one_edge = None
    for node in graph:
        if len(graph[node]) == 1:
            if nodes_with_one_edge == None:
                nodes_with_one_edge = [node]
            else:
                nodes_with_one_edge.append(node)

    if nodes_with_one_edge != None and len(nodes_with_one_edge) > 2:
        return False
    if nodes_with_one_edge != None and len(nodes_with_one_edge) == 2:
        for edge1, edge2 in zip(graph[nodes_with_one_edge[0]], graph[nodes_with_one_edge[1]]):
            if edge1 != edge2:
                return False

    i = 2
    for node in graph:
        if len(graph[node]) == 1:
            for edge, value in graph[node].items():
                if value[1] == 0:
                    value[1] = 1
                    graph[value[0]][edge][1] = 1
                break
        else:
            for edge, value in graph[node].items():
                if value[1] == 0:
                    value[1] = i
                    graph[value[0]][edge][1] = i
                    i += 1

    print(graph)
    return


file = open("input.txt", "r")
n, m = map(int, file.readline().split())

graph = {}
for i in range(1, m + 1):
    u, v = map(int, file.readline().split())

    if u in graph:
        graph[u][i] = [v, 0]
    else:
        graph[u] = {i: [v, 0]}
    if v in graph:
        graph[v][i] = [u, 0]
    else:
        graph[v] = {i: [u, 0]}
file.close()

print(graph)
weight_edges(graph, m)
