# [2, 0, 2, 1, 1, 0]
def sortColors(nums):
    # i = l = 0
    # j = r = len(nums) - 1
    # while l < r:
    #     if nums[i] == 0:
    #         if l != i:
    #             nums[i], nums[l] = nums[l], nums[i]
    #         l += 1
    #         i += 1
    #         continue
    #     if nums[j] == 2:
    #         if r != j:
    #             nums[j], nums[r] = nums[r], nums[j]
    #         r -= 1
    #         j -= 1
    #         continue
    #     if nums[i] == 2 and r >= 0 and i <= r:
    #         nums[i], nums[r] = nums[r], nums[i]
    #         if j == r:
    #             j -= 1
    #         r -= 1
    #         if l == i and nums[l] == 0:
    #             l += 1
    #         i += 1
    #         continue
    #     if nums[j] == 0 and l < len(nums) and j >= l:
    #         nums[j], nums[l] = nums[l], nums[j]
    #         if i == l:
    #             i += 1
    #         l += 1
    #         if r == j and nums[r] == 2:
    #             r -= 1
    #         j -= 1
    #         continue

    # l = 0
    # r = len(nums) - 1
    # for i in range(0, len(nums)):
    #     while nums[i] == 2 and i < r:
    #         nums[i], nums[r] = nums[r], nums[i]
    #         r -= 1
    #     while nums[i] == 0 and i > l:
    #         nums[i], nums[l] = nums[l], nums[i]
    #         l += 1

    i = 0
    l = 0
    r = len(nums) - 1
    while i <= r:
        while l < len(nums) and nums[l] == 0:
            l += 1
        while r >= 0 and nums[r] == 2:
            r -= 1

        if nums[i] == 0:
            if i > l:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                continue
        elif nums[i] == 2:
            if i < r:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                continue
        i += 1
    print(nums)


# sortColors([2, 0, 2, 1, 1, 0])
# sortColors([2, 0, 2, 2, 1, 0, 1])
# sortColors([0])
# sortColors([0, 0, 1])
sortColors([0, 2, 2, 2, 0, 2, 1, 1])
