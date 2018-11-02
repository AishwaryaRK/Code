def max_value(items, w):
    if len(items) == 0 or w == 0:
        return 0
    if items[0][1] > w:
        return max_value(items[1:], w)
    return max(max_value(items[1:], w), max_value(items[1:], w - items[0][1]) + items[0][0])


print(max_value([(65, 20), (35, 8), (245, 60), (195, 55),
                 (65, 40), (150, 70), (275, 85), (155, 25),
                 (120, 30), (320, 65), (75, 75), (40, 10), (200, 95),
                 (100, 50), (220, 40), (99, 10)], 130))
