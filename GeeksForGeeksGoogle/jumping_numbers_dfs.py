def jumping_numbers(n):
    nums = ['0']

    for d in range(1, 10):
        queue = []
        queue.append(str(d))
        while len(queue) != 0:
            num = queue.pop(0)
            if int(num) <= n:
                nums.append(num)
            if len(num) + 1 <= len(str(n)):
                last_digit = int(num[-1])
                prev = last_digit - 1
                next = last_digit + 1
                if prev >= 0:
                    queue.append(num + str(prev))
                if next < 10:
                    queue.append(num + str(next))
    return nums


t = int(input())
for i in range(0, t):
    n = int(input())
    print(*jumping_numbers(n))
