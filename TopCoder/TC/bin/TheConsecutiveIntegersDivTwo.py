class TheConsecutiveIntegersDivTwo:
    def find(self, numbers, k):
        if k == 1:
            return 0
        diff = None
        sorted_numbers = sorted(numbers)
        for n in numbers:
            i = sorted_numbers.index(n)
            if i - 1 >= 0 and (diff == None or abs(n - sorted_numbers[i - 1]) <= diff):
                diff = abs(n - sorted_numbers[i - 1])
            if i + 1 < len(sorted_numbers) and (diff == None or abs(n - sorted_numbers[i + 1]) <= diff):
                diff = abs(n - sorted_numbers[i + 1])
        return diff - 1


print(TheConsecutiveIntegersDivTwo().find({-96, -53, 82, -24, 6, -75}, 2))
