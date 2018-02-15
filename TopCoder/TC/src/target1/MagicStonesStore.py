class MagicStonesStore:
    def ableToDivide(self, n):
        c = 2 * n
        for a in range(2, c):
            b = c - a
            print(a, b, self.isPrime(a), self.isPrime(b))
            if self.isPrime(a) and self.isPrime(b):
                return "YES"
        return "NO"

    def isPrime(self, num):
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                return False
        return True


print(MagicStonesStore().ableToDivide(3))
