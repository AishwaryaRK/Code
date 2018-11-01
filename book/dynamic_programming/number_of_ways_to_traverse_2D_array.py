ways = {'0,0': 1}


def number_of_ways_to_traverse_2D_array(m, n):
    if str(m) + "," + str(n) in ways:
        return ways[str(m) + "," + str(n)]
    if m == 0 and n > 0:
        w = number_of_ways_to_traverse_2D_array(m, n - 1)
    elif n == 0 and m > 0:
        w = number_of_ways_to_traverse_2D_array(m - 1, n)
    else:
        w = number_of_ways_to_traverse_2D_array(m - 1, n) + number_of_ways_to_traverse_2D_array(m, n - 1)

    ways[str(m) + "," + str(n)] = w
    return w


print(number_of_ways_to_traverse_2D_array(4, 4))
print(ways)
