def sum_four_numbers(nums, sum):
    pairs_sum = {}
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            s = nums[i] + nums[j]
            pairs_sum[s] = (nums[i], nums[j])

    numbers = []
    for k, v in pairs_sum.items():
        k2 = sum - k
        if k2 in pairs_sum:
            n = [pairs_sum[k][0], pairs_sum[k][1], pairs_sum[k2][0], pairs_sum[k2][1]]
            if len(set(n)) == len(n):
                numbers.append(sorted(n))

    numbers = [tuple(e) for e in numbers]
    numbers = set(numbers)
    numbers = [list(e) for e in numbers]
    return numbers


t = int(input())
for i in range(0, t):
    n, k = map(int, input().split(' '))
    nums = list(map(int, input().strip().split(' ')))
    numbers = sum_four_numbers(nums, k)
    if len(numbers)==0:
        print(-1)
    else:
        for l in numbers:
            print(*l, end='')
            print(' $', end='')
