def maxArea(heights):
    i = 0
    j = len(heights) - 1
    area = 0
    while i < j:
        if heights[i] > heights[j]:
            a = heights[j] * (j - i)
            j -= 1
        else:
            a = heights[i] * (j - i)
            i += 1
        if a > area:
            area = a
    return area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
