# Given an array of positive numbers and a positive number ‘S’,
# find the length of the smallest subarray whose sum is greater than or equal to ‘S’.
# Return 0, if no such subarray exists.

import math

def smallest_subarray_with_given_sum(s1, arr):
    c = 1
    min_c = math.inf
    i = 0
    s = arr[0]
    for j in range(1, len(arr)):
        if s > s1:
            s = s - arr[i]
            i += 1
            c -= 1
        if s == s1:
            if c < min_c:
                min_c = c

        s += arr[j]
        c += 1

    return 0 if min_c == math.inf else min_c


def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
