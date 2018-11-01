import math


class Solution:
    def findRotateSteps(self, ring, key):
        cnt = 0
        l = len(ring)
        mid_len = math.floor(l / 2)
        for k in key:
            print("--------- ", k, ring)
            if ring[0] == k:
                cnt += 1
            else:
                right = ring[0:mid_len + 1]
                left = ring[mid_len + 1:][::-1]

                print(right, left)
                a = b = None
                i = right.find(k)
                if i != -1:
                    a = i
                i = left.find(k)
                if i != -1:
                    b = i

                print(a, b)
                if a == None:
                    cnt += b + 1 + 1
                    ring = left[:b + 1][::-1] + right + left[b + 1:][::-1]
                elif b == None:
                    cnt += a + 1
                    ring = right[a:] + left[::-1] + right[:a]
                elif a <= b:
                    cnt += a + 1
                    ring = right[a:] + left[::-1] + right[:a]
                else:
                    cnt += b + 1 + 1
                    ring = left[:b + 1][::-1] + right + left[b + 1:][::-1]
            print(cnt)

        return cnt


# print(Solution().findRotateSteps("godding", "gd"))
# print(Solution().findRotateSteps("godding", "godding"))
# print(Solution().findRotateSteps("abcde", "ade"))
# print(Solution().findRotateSteps("edcba", "abcde"))
print(Solution().findRotateSteps("iotfo", "fioot"))
