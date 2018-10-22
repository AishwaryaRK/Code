import math


class Solution:
    def countBits(self, num):
        bits = [0]
        if num == 0:
            return bits
        i = 0
        n = 1
        ep = 1
        while True:
            e = int(math.pow(2, i))
            while n <= e:
                if e == n:
                    bits.append(1)
                else:
                    bits.append(bits[ep] + bits[n - ep])
                if n == num:
                    return bits
                n += 1

            ep = e
            i += 1


print(Solution().countBits(5))
