def index_equals_value_search(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        mid = int(i + (j - i) / 2)
        if arr[mid] == mid:
            return mid
        if arr[mid] > mid:
            j = mid - 1
        else:
            i = mid + 1
    return -1

    # for i, a in enumerate(arr):
    #     if i == a:
    #         return i
    #     if a > i:
    #         return -1
    #
    # return -1