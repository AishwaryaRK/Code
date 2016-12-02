class LiveConcert:
    def maxHappiness(self, h, s):
        happiness = []
        grps = set(s)
        for i, idolGrp in enumerate(grps):
            happinessVal = 0
            for index, idol in enumerate(s):
                if idol == idolGrp and happinessVal < h[index]:
                    happinessVal = h[index]
            happiness.append(happinessVal)
                # grps = filter(lambda e: e != idolGrp, s)  # [e for e in s if e!= idolGrp]
        print happiness
        return sum(happiness)


print LiveConcert().maxHappiness((10, 5, 6, 7, 1, 2), ("ciel", "bessie", "john", "bessie", "bessie", "john"))


s = [ 111, 22 ]
even = []
for num in s:
    if s % 2 == 0:
        even.append(num)

list comprehension

s = [[1, 2], [3, 4]]
output = [[1, 4], [9, 16]]

output = [[num*num for num in l] for l in s]

def is_even(x):
    return x % 2 == 0

even = filter(lambda x: x % 2 == 0, s)
even = [num for num in s if s % 2 == 0]

d = {1: 1, 2: 4, 3: 9}
d = {x: x*x for x in s}

s = [("aishwarya", 50), ("sid", 25)]
d = {x[0]: x[1] for x in s}

even_set = set(x for x in s if x % 2 == 0)

