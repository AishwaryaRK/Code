def get_kth_divisor(n, k):
    if k > n / 2 + 1:
        return -1
    count = 1
    kth_divisor = 1
    for i in xrange(2, n / 2 + 1):
        if count == k:
            break
        if n % i == 0:
            kth_divisor = i
            count += 1
    return kth_divisor if count == k else -1


str = raw_input()
n = int(str.split(" ")[0])
k = int(str.split(" ")[1])
print get_kth_divisor(n, k)
