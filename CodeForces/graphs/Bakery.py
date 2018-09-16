def get_min_amt(graph, storage_cities, n, k):
    min_amt = None
    for storage_city in storage_cities:
        if storage_city in graph:
            for node in graph[storage_city]:
                if node not in storage_cities:
                    d = graph[storage_city][node]
                    if min_amt == None or d < min_amt:
                        min_amt = d

    return -1 if min_amt == None else min_amt


def main():
    n, m, k = map(int, input().split())
    if k == 0:
        print(-1)
        return

    graph = {}
    for i in range(0, m):
        u, v, l = map(int, input().split())
        if u in graph:
            value = graph[u]
            if v in value:
                if l < value[v]:
                    value[v] = l
                    graph[u] = value
            else:
                value[v] = l
                graph[u] = value
        else:
            graph[u] = {v: l}
        if v in graph:
            value = graph[v]
            if u in value:
                if l < value[u]:
                    value[u] = l
                    graph[v] = value
            else:
                value[u] = l
                graph[v] = value
        else:
            graph[v] = {u: l}

    storage_cities = list(map(int, input().split()))
    # bakery_cities = list(set(range(1, n + 1)) - set(storage_cities))
    # print(bakery_cities, storage_cities)
    # print(graph)
    print(get_min_amt(graph, storage_cities, n, k))


main()
