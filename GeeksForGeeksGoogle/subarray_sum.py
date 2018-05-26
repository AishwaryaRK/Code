def subarray_sum(n, s, numbers):
    start = 0
    sum = 0
    i = 0
    while i < n:
        while sum < s and i < n:
            sum += numbers[i]
            if sum == s:
                print(str(start + 1) + " " + str(i + 1))
                return
            i += 1
        while sum > s:
            sum -= numbers[start]
            start += 1
            if sum == s:
                print(str(start + 1) + " " + str(i))
                return
    print(-1)


t = int(input().strip())
for i in range(0, t):
    n, s = map(int, input().strip().split(' '))
    numbers = list(map(int, input().strip().split(' ')))
    subarray_sum(n, s, numbers)
