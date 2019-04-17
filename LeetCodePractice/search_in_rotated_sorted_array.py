def search(nums, target):
    i = 0
    j = len(nums) - 1
    while i <= j:
        mid = int(i + (j - i) / 2)
        if nums[mid] == target:
            return mid
        if nums[mid] <= nums[j]:
            if nums[mid] < target <= nums[j]:
                i = mid + 1
            else:
                j = mid - 1
        elif nums[i] <= nums[mid]:
            if nums[i] <= target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1

    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([1, 3], 3))
print(search([4, 5, 6, 7, 0, 1, 2], 3))
