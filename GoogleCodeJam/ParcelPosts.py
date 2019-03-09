def count_posts(a):
    cnt = 0

    post = 0
    i = 0
    j = 2
    while i < len(a):
        if i + j < len(a):
            x = i + 1
            flag = False
            while x < i + j and not flag:
                if (a[x] < a[i] and a[x] < a[i + j]) or (a[x] > a[i] and a[x] > a[i + j]):
                    i += j
                    post = i
                    cnt += 1
                    j = 2
                    flag = True
                x += 1
            if not flag:
                j += 1

        elif post == i:
            cnt -= 1
            break

    return cnt


T = int(input())
for n in range(1, T + 1):
    k = int(input())
    a = list(map(int, input().split(" ")))
    cnt = count_posts(a)
    print("Case #" + str(n) + ": " + str(cnt))
