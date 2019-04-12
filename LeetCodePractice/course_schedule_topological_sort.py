# 4, [[1,0],[2,0],[3,1],[3,2]]

# 3->1->0
#  \    ^
#   \   |
#    \> 2

# 1,0,2,3
# stack  3
#
# 0 1 2 3

# 1,0
# stack  1
# 0
#

# def findOrder(numCourses, prerequisites):
#     if len(prerequisites) == 0:
#         order = []
#         for i in range(0, numCourses):
#             order.append(i)
#         return order
#
#     edges = {}
#     for prerequisite in prerequisites:
#         if prerequisite[0] not in edges:
#             edges[prerequisite[0]] = [prerequisite[1]]
#         else:
#             v = edges[prerequisite[0]]
#             v.append(prerequisite[1])
#             edges[prerequisite[0]] = v
#
#     visited = {}
#     stack = []
#     order = []
#     while len(edges) != 0:
#         edge_u = list(edges.keys())[0]
#         if len(stack) == 0:
#             if edge_u not in visited:
#                 stack.append(edge_u)
#                 visited[edge_u] = 1
#         else:
#             u = stack[-1]
#             flag = True
#             if u in edges:
#                 for v in edges[u]:
#                     if v not in visited:
#                         visited[v] = 1
#                         stack.append(v)
#                         flag = False
#                     else:
#                         if v in edges and u in edges[v]:
#                             return []
#             if flag:
#                 order.append(u)
#                 stack.pop()
#                 if u in edges:
#                     del edges[u]
#
#     for i in range(0, numCourses):
#         if i not in order:
#             order.append(i)
#     return order

def findOrder(numCourses, prerequisites):
    if len(prerequisites) == 0:
        order = []
        for i in range(0, numCourses):
            order.append(i)
        return order

    edges = {}
    for prerequisite in prerequisites:
        if prerequisite[0] == prerequisite[1]:
            return []
        if prerequisite[0] not in edges:
            edges[prerequisite[0]] = [prerequisite[1]]
        else:
            v = edges[prerequisite[0]]
            v.append(prerequisite[1])
            edges[prerequisite[0]] = v

    visited = {}
    stack = []
    order = []
    for vertex in edges.keys():
        if vertex not in visited:
            stack.append(vertex)
            visited[vertex] = 1
        while len(stack) != 0:
            v = stack.pop()
            if v not in edges:
                order.append(v)
            else:
                flag = True
                stack.append(v)
                for u in edges[v]:
                    if u in visited:
                        if u in edges and v in edges[u]:
                            return []
                    else:
                        visited[u] = 1
                        stack.append(u)
                        flag = False
                if flag:
                    stack.pop()
                    order.append(v)
    print(order)
    for v in range(0, numCourses):
        if v not in order:
            order.append(v)

    return order[::-1]


print(findOrder(2, [[1, 0]]))
# print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
