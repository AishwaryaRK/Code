import math


class PalindromePrime:
    def count(self, L, R):
        count = 0
        for n in range(L, R + 1, 1):
            if not self.isConsonant(n) and self.isPalindrome(n):
                print n
                count += 1
        return count

    def isConsonant(self, n):
        return True if n == 1 else any(n % i == 0 for i in range(2, n, 1))

    def isPalindrome(self, n):
        if str(n)[::-1] == str(n):
            return True
        return False


# print  PalindromePrime().isConsonant(337)
print PalindromePrime().count(1, 9)
