from functools import reduce


class Cryptography:
    def encrypt(self, numbers):
        numbers = sorted(numbers)
        numbers[0] += 1
        return reduce(lambda x, y: x * y, numbers)


print(Cryptography().encrypt({1, 2, 3}))
