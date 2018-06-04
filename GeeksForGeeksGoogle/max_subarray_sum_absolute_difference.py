def get_max_subarray_sum_absolute_difference(a):
    max_left = []
    max_right = []
    min_left = []
    min_right = []

    for i in range(0, len(a) - 1):
        max_left.append(find_max_subarray_sum(a[0:i + 1]))
        min_left.append(find_min_subarray_sum(a[0:i + 1]))
        max_right.append(find_max_subarray_sum(a[i + 1:]))
        min_right.append(find_min_subarray_sum(a[i + 1:]))

    absolute_max = None
    for i in range(0, len(a) - 1):
        if absolute_max == None or abs(max_left[i] - min_right[i]) > absolute_max:
            absolute_max = abs(max_left[i] - min_right[i])
        if abs(max_right[i] - min_left[i]) > absolute_max:
            absolute_max = abs(max_right[i] - min_left[i])

    return absolute_max


def find_max_subarray_sum(a):
    prev_max = None
    max_sum = a[0]
    for i in range(0, len(a)):
        prev_max = a[i] if prev_max == None or a[i] > prev_max + a[i] else prev_max + a[i]
        if prev_max > max_sum:
            max_sum = prev_max
    return max_sum


def find_min_subarray_sum(a):
    prev_min = None
    min_sum = a[0]
    for i in range(0, len(a)):
        prev_min = a[i] if prev_min == None or a[i] < prev_min + a[i] else prev_min + a[i]
        if prev_min < min_sum:
            min_sum = prev_min
    return min_sum


t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().strip().split(' ')))
    print(get_max_subarray_sum_absolute_difference(a))
