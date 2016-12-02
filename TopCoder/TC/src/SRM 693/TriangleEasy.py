class TriangleEasy:
    def find(self, n, x, y):
        if len(x) == 0:
            return 3
        nodes = [[] for _ in range(n)]
        for a, b in zip(x, y):
            print a, b
            nodes[a].append(b)
            nodes[b].append(a)
        doubles = [index for index, node in enumerate(nodes) if len(node) > 1]
        if len(doubles) == 0:
            return 2
        for node in doubles:
            for a in nodes[node]:
                for b in nodes[a]:
                    if b != node and node in nodes[b]:
                        return 0
        return 1


print TriangleEasy().find(4, (0, 2), (1, 3))
