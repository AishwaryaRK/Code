def searchRange(nums, target):
    if len(nums) == 0:
        return [-1, -1]

    i = binary_search(nums, target, 0, len(nums) - 1)
    if i == -1:
        return [-1, -1]

    left = i
    while True:
        if left - 1 < 0:
            break
        left_most_index = binary_search(nums, target, 0, left - 1)
        if left_most_index == -1:
            break
        left = left_most_index

    right = i
    while True:
        if right + 1 >= len(nums):
            break
        right_most_index = binary_search(nums, target, right + 1, len(nums) - 1)
        if right_most_index == -1:
            break
        right = right_most_index

    return [left, right]


def binary_search(nums, target, i, j):
    while i <= j:
        mid = int(i + (j - i) / 2)
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            j = mid - 1
        else:
            i = mid + 1

    return -1


# print(searchRange([5, 7, 7, 8, 8, 10], 8))
# print(searchRange([5, 7, 7, 8, 8, 10], 6))
print(searchRange([2, 2], 3))
