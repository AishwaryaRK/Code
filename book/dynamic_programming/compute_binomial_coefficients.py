cache = {}


def compute_binomial_coefficients(n, k):
    if k == 1:
        return n
    if k == 0 or n == k:
        return 1

    key = str(n - 1) + "," + str(k - 1)
    w = cache[key] if key in cache else compute_binomial_coefficients(n - 1, k - 1)
    cache[key] = w

    key = str(n - 1) + "," + str(k)
    wo = cache[key] if key in cache else compute_binomial_coefficients(n - 1, k)
    cache[key] = wo

    return w + wo


print(compute_binomial_coefficients(5, 2))
print(compute_binomial_coefficients(167, 58))
