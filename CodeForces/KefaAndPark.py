def get_paths(m, cats, tree, root, prev_consecutive_cats):
    global visited
    visited.append(root)
    if cats[root - 1] == 0:
        prev_consecutive_cats = 0
    else:
        prev_consecutive_cats += 1

    if prev_consecutive_cats > m:
        return 0

    if len(tree[root]) == 1 and root != 1:
        if prev_consecutive_cats <= m:
            return 1
        else:
            return 0

    cnt = 0
    for child in tree[root]:
        if child not in visited:
            visited.append(child)
            cnt += get_paths(m, cats, tree, child, prev_consecutive_cats)
    return cnt


n, m = map(int, input().split())
cats = list(map(int, input().split()))
tree = {}
visited = []
for i in range(1, n):
    u, v = map(int, input().split())
    if u not in tree:
        tree[u] = [v]
    else:
        tree[u].append(v)
    if v not in tree:
        tree[v] = [u]
    else:
        tree[v].append(u)

# print(tree)
print(get_paths(m, cats, tree, 1, 0))

# n = 7
# m = 1
# cats = [1, 0, 1, 1, 0, 0, 0]
# tree = {1: [2, 3], 2: [1, 4, 5], 3: [1, 6, 7], 4: [2], 5: [2], 6: [3], 7: [3]}
# visited = []
# print(get_paths(m, cats, tree, 1, 0))
