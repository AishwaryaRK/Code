def get_max(n, numbers):
    max = 1
    for i, num in enumerate(numbers):
        if i == n - 1:
            return max
        d = 2 * num
        index = find_index(n, i, d, numbers)
        c = index - i + 1
        # for j in range(i + 1, n):
        #     if numbers[j] <= d:
        #         c += 1
        #     else:
        #         break
        if c > max:
            max = c
    return max


def find_index(n, pivot, d, numbers):
    last = numbers[-1]
    if last <= d:
        return n - 1
    if numbers[pivot + 1] > d:
        return pivot

    i = int((pivot + 1 + n - 1) / 2)
    while True:
        if numbers[i] <= d and numbers[i + 1] > d:
            return i
        if numbers[i] > d and i - 1 >= pivot and numbers[i - 1] <= d:
            return i - 1
        if numbers[i] <= d:
            if i + 1 == n - 1:
                # if numbers[i + 1] <= d:
                #     return i + 1
                # else:
                return i
            i = int((i + n - 1) / 2)
        else:
            # if i - 1 == pivot:
            #     return pivot
            i = int((pivot + 1 + i) / 2)


n = int(input())
numbers = list(map(int, input().split()))
print(get_max(n, numbers))
