
def get_height(root, forest):
    heights = []
    for child in forest[root]:
        heights.append(1 + get_height(child, forest))
    if heights == []:
        return 1
    return max(heights)


n = int(input())
forest = {}
roots = []
for i in range(1, n + 1):
    m = int(input())
    if i not in forest:
        forest[i] = []
    if m == -1:
        roots.append(i)
    elif m in forest:
        forest[m].append(i)
    else:
        forest[m] = [i]

max_heights = []
for root in roots:
    max_heights.append(get_height(root, forest))

print(max(max_heights))


# def is_present(tree, m, i):
#     if m in tree:
#         tree[m][i] = {}
#         return True
#     for f in tree:
#         if is_present(tree[f], m, i):
#             return True
#     return False
#
#
# def get_max_len(forest):
#     if forest == {}:
#         return 0
#     heights = []
#     for tree in forest:
#         heights.append(1 + get_max_len(forest[tree]))
#     return max(heights)
#
# n = int(input())
# forest = {}
# roots = {}
# for i in range(1, n + 1):
#     m = int(input())
#     if m == -1:
#         forest[i] = {}
#         roots[i] = "root"
#     else:
#         root = "root"
#         if m in forest:
#             forest[m][i] = {}
#             roots[i] = m
#         else:
#             for f in forest:
#                 if is_present(forest[f], m, i):
#                     root = f
#                     break
#             roots[i] = root
#             if root == "root":
#                 forest[i] = {}
#
# print(forest)
# print(get_max_len(forest))
