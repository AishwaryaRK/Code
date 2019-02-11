def largest_rect_under_skyline(heights):
    buildings_heights = {}
    cnts_heights = {}
    largest_rect_area = 0

    for i, ht in enumerate(heights):
        for h in range(1, ht + 1):
            if h not in buildings_heights:
                buildings_heights[h] = i
                cnts_heights[h] = [1, 0]
            else:
                if buildings_heights[h] + 1 == i:
                    cnts_heights[h][0] += 1
                else:
                    cnts_heights[h][1] = max(cnts_heights[h][1], cnts_heights[h][0])
                    cnts_heights[h][0] = 1
                buildings_heights[h] = i

            area = h * max(cnts_heights[h][1], cnts_heights[h][0])
            largest_rect_area = max(largest_rect_area, area)

    print(cnts_heights)

    return largest_rect_area


print(largest_rect_under_skyline([1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]))
