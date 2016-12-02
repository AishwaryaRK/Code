import math


def getDistance(sciNotationNum):
    a, b = sciNotationNum.split("e")
    if '.' not in a:
        for i in range(1, b + 1):
            a = a + '0'
        return a
    a = a.rstrip('0')
    b = int(b) - len(a.split('.')[1])
    a = a.replace('.', '')
    if b == 0:
        return a
    if b > 0:
        for i in range(1, b + 1):
            a = a + '0'
        return a
    else:
        return a[0:b] + '.' + a[b:]


# num = float("{0:.6f}".format(a * math.pow(10, b)))
# return int(num) if int(num) == num else str(num).rstrip('0')

sciNotationNum = input()
# sciNotationNum = "4.28522890224373996236468418851564462623381500262405e30"
print(getDistance(sciNotationNum))
