def findDuplicate(nums):
    # s1 = sum(nums)
    # n = len(nums) - 1
    # s2 = ((n + 1) * n) / 2
    # return s2 - s1

    # [3, 1, 3, 4, 2]
    # cnt = 1
    # n = nums[0]
    # for i in range(1, len(nums)):
    #     if cnt == 0:
    #         cnt = 1
    #         n = nums[i]
    #     elif nums[i] == n:
    #         cnt += 1
    #     else:
    #         cnt -= 1
    # return n
    # [1, 3, 4, 2, 2]

    slow_p = nums[0]
    fast_p = nums[0]
    while True:
        slow_p = nums[slow_p]
        fast_p = nums[fast_p]
        fast_p = nums[fast_p]
        if fast_p == slow_p:
            break

    print(slow_p)
    slow1_p = nums[0]
    while True:
        if slow_p == slow1_p:
            return slow_p
        slow_p = nums[slow_p]
        slow1_p = nums[slow1_p]



print(findDuplicate([3, 1, 3, 4, 2]))
