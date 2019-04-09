def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    max_length = 1
    lengths = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                lengths[i] = max(lengths[i], 1 + lengths[j])
        if lengths[i] > max_length:
            max_length = lengths[i]
    return max_length