def highest_product(numbers):
    h1 = h2 = l1 = l2 = 0
    highest_product = 0
    for n in numbers:
        print(h1, h2, l1, l2, highest_product, n)
        if h1 * h2 * n >= highest_product:
            highest_product = h1 * h2 * n
        if l1 * l2 * n >= highest_product:
            highest_product = l1 * l2 * n
        if n >= h1:
            h2 = h1
            h1 = n
        elif n >= h2:
            h2 = n
        print(n <= l1)
        if n <= l1:
            l2 = l1
            l1 = n
        elif n <= l2:
            l2 = n
    return max(highest_product, l1 * l2 * h1)


print(highest_product([1, 10, -5, 1, -100]))
