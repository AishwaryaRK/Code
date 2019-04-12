def findPeakElementIndex(nums):
    if len(nums) == 1:
        return 0
    l = 0
    h = len(nums) - 1
    while True:
        mid = int(l + (h - l) / 2)
        if mid == 0:
            if nums[mid] > nums[mid + 1]:
                return mid
            else:
                l = mid + 1
        elif mid == len(nums) - 1:
            if nums[mid] > nums[mid - 1]:
                return mid
            else:
                h = mid - 1
        elif nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return mid
        elif nums[mid + 1] > nums[mid]:
            l = mid + 1
        elif nums[mid - 1] > nums[mid]:
            h = mid - 1

print(findPeakElementIndex([1,2]))