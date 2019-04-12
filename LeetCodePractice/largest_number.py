import functools

def comparator(x, y):
    if int(x + y) > int(y + x):
        return 1
    return -1


def largestNumber(nums):
    if all(n==0 for n in nums):
        return '0'

    a = []
    for n in nums:
        a.append(str(n))

    return ''.join(sorted(a, reverse=True, key=functools.cmp_to_key(comparator)))

print(largestNumber([3, 30, 34, 5, 9]))
