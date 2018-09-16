def queue_at_t(q, n, t):
    q = list(q)
    for j in range(0, t):
        i = 0
        while i < n - 1:
            if q[i] == 'B' and q[i + 1] == 'G':
                q[i] = 'G'
                q[i + 1] = 'B'
                i += 2
            else:
                i += 1
    return ''.join(q)


n, t = map(int, input().split())
q = input()
print(queue_at_t(q, n, t))
