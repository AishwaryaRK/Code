def ladderLength(beginWord, endWord, wordList):
    stack = [beginWord]
    graph = {}
    visited = {}
    while len(stack) != 0:
        word = stack.pop()
        visited[word] = 1
        nodes = []
        for w in wordList:
            if w not in visited:
                if is_one_edit_distance(word, w):
                    nodes.append(w)
                    stack.append(w)
        graph[word] = nodes

    l = 1
    queue = [[beginWord]]
    while len(queue) != 0:
        nodes = []
        for node in queue.pop():
            if node in graph and endWord in graph[node]:
                l += 1
                return l
            nodes += graph[node]
        l += 1
        queue.append(nodes)

    return 0


def is_one_edit_distance(w1, w2):
    l = 0
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            l += 1
        if l > 1:
            return False
    return True


print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
