def wcd(nums, m):
    for d in range(2, m + 1):
        flag = True
        for n in nums:
            if n % d != 0:
                flag = False
                break
        if flag:
            return d

    return -1


n = int(input())
nums = []
m = None
for i in range(0, n):
    a, b = map(int, input().split())
    k = a * b
    if m == None or k < m:
        m = k
    nums.append(k)

print(wcd(nums, m))
