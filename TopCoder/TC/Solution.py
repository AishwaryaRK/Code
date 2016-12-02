import math

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        a = A / 2
        for i in range(a, 0, -1):
            if i * i <= A:
                return i

input = int(raw_input())
print input
print Solution().sqrt(input)
print math.sqrt(input)