from collections import deque


class Solution:
    def addTwoNumbers(self, l1, l2):
        l1.reverse()
        num1 = ""
        for n in l1:
            num1 += str(n)
        l2.reverse()
        num2 = ""
        for n in l2:
            num2 += str(n)

        num3 = int(num1) + int(num2)
        l = [int(n) for n in reversed(str(num3))]
        return deque(l)


print(Solution().addTwoNumbers(deque([2, 4, 3]), deque([5, 6, 4])))
