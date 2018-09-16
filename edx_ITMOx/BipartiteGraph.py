def is_bipartite_graph(graph):
    subset1 = {}
    subset2 = {}

    for u in graph:
        u_subset = None
        v_subset = None
        if u in subset1:
            u_subset = subset1
            v_subset = subset2
        elif u in subset2:
            u_subset = subset2
            v_subset = subset1
        for v in graph[u]:
            if v_subset != None:
                if v in u_subset:
                    return False
                for n in graph[v]:
                    if n in v_subset:
                        return False
                v_subset[v] = True
            else:
                if is_bipartite_valid(graph[u], subset1) and is_bipartite_valid(graph[v], subset2):
                    subset1[u] = True
                    subset2[v] = True
                elif is_bipartite_valid(graph[u], subset2) and is_bipartite_valid(graph[v], subset1):
                    subset2[u] = True
                    subset1[v] = True
                else:
                    return False

    return True


def is_bipartite_valid(nodes, subset):
    for n in nodes:
        if n in subset:
            return False
    return True


file = open("input.txt", "r")
n, m = map(int, file.readline().split())

graph = {}
flag = True
for i in range(0, m):
    u, v = map(int, file.readline().split())

    if u == v:
        file1 = open("output.txt", "w")
        file1.write("YES")
        file1.close()
        flag = False
        break

    if u in graph:
        value = graph[u]
        value[v] = True
        graph[u] = value
    else:
        graph[u] = {v: True}
    if v in graph:
        value = graph[v]
        value[u] = True
        graph[v] = value
    else:
        graph[v] = {u: True}

file.close()

if flag:
    file1 = open("output.txt", "w")
    if is_bipartite_graph(graph):
        file1.write("YES")
    else:
        file1.write("NO")
    file1.close()
