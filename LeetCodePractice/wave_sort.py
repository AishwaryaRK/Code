def wiggleSort(nums):
    # for i in range(1, len(nums), 2):
    #     if i == len(nums) - 1:
    #         if nums[i] < nums[i - 1]:
    #             nums[i], nums[i - 1] = nums[i - 1], nums[i]
    #     else:
    #         if nums[i] < nums[i - 1]:
    #             nums[i], nums[i - 1] = nums[i - 1], nums[i]
    #         if nums[i] < nums[i + 1]:
    #             nums[i], nums[i + 1] = nums[i + 1], nums[i]

    for i in range(0, len(nums)-1):
        if i%2==0:
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        else:
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    print(nums)


wiggleSort([1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2])
