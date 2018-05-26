import collections


def find(numbers):
    freq = collections.Counter(numbers)
    print(freq)
    return [k for k, v in freq.items() if v % 2 == 1]


t = int(input().strip())
for i in range(0, t):
    n = int(input().strip())
    numbers = list(map(int, input().strip().split(' ')))
    print(numbers)
    nums = find(numbers)
    print(nums)
    nums.sort()
    print(*nums)
