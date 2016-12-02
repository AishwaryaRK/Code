def cost(arr):
    min = 200
    # for i, a1 in enumerate(arr):
    #     for j, a2 in enumerate(arr):
    #         if i != j:
    #             if a1 == a2:
    #                 return 0
    #             if abs(a1 - a2) < min:
    #                 min = abs(a1 - a2)
    arr = sorted(arr)
    l = len(arr)
    for i in range(1, l):
        if arr[i] - arr[i - 1] <= min:
            min = arr[i] - arr[i - 1]
    return min


# print(cost([4, 2, 10]))


def maxElement(arr):
    arr = sorted(arr, reverse=True)
    l = len(arr)
    print(arr)
    for i in range(0, l - 1):
        for j in range(i + 1, l - 1):
            n2 = int(arr[i] / arr[j])
            if arr[i] % arr[j] == 0 and n2 <= arr[j + 1] and n2 in arr[j + 1:]:
                return arr[i]
    return -1


print(maxElement([2, 4, 8, 6]))
