class TriangleEasy:
    def find(self, n, x, y):
        if not x:
            return 3

        graph = {}

        for a, b in zip(x, y):
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]
            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]

        least_count = 2

        for first_node, v in graph.items():
            for second_node in v:
                if len(graph[second_node])>1:
                    for third_node in graph[second_node]:
                        if third_node in v:
                            return 0
                        else:
                            least_count = 1

        return least_count


print(TriangleEasy().find(3,
                          [0,2],
                          [1,3]))


# print(TriangleEasy().find(20,
#                           [16, 4, 15, 6, 1, 0, 10, 12, 7, 15, 2, 4, 8, 1, 10, 15, 13, 10, 1, 16, 3, 19, 8, 7, 13, 1, 15,
#                            15, 15, 5, 16, 7, 5, 6, 4, 18, 3, 8, 6, 2, 16, 8, 19, 14, 17, 16, 4, 6, 9, 17, 4, 10, 8, 12,
#                            2, 3, 18, 9, 13, 17, 4, 7, 10, 0, 13, 11, 15, 17, 11, 15, 11, 19, 19, 4, 10, 14, 16, 6, 3,
#                            17, 1, 4, 14, 9, 7, 18, 10, 11, 5, 0, 5, 9, 9, 7, 16, 12, 4, 10, 17, 3],
#                           [17, 18, 6, 16, 18, 6, 11, 2, 15, 10, 1, 15, 17, 8, 5, 9, 7, 0, 0, 4, 16, 1, 9, 0, 9, 5, 17,
#                            14, 1, 12, 14, 11, 9, 18, 0, 12, 11, 3, 19, 14, 7, 6, 3, 19, 0, 1, 19, 5, 11, 19, 2, 13, 12,
#                            0, 6, 2, 14, 16, 14, 18, 5, 5, 19, 3, 6, 14, 12, 5, 17, 3, 1, 12, 7, 11, 8, 8, 10, 11, 13, 2,
#                            13, 13, 0, 18, 2, 7, 2, 12, 14, 9, 3, 19, 2, 8, 12, 13, 8, 18, 13, 18]
#                           ))
