class Cdgame:
    def rescount(self, a, b):
        sumA = sum(a)
        sumB = sum(b)
        products = []
        for i in a:
            for j in b:
                products.append((sumA - i + j) * (sumB - j + i))
        return len(set(products))


print Cdgame().rescount((1, 2), (3, 4))
