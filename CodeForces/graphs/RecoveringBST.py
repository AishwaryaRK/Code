import math


def isBST(tree):
    root = tree[0]
    bst = {root: (None, None)}
    for i in range(1,len(tree)):
        n=tree[i]
        r = root
        while True:
            c = bst[r]
            if n <= r:
                if c[0] == None and math.gcd(r, n) > 1:
                    bst[r] = (n, c[1])
                    bst[n] = (None, None)
                    break
                elif c[0] != None:
                    r = c[0]
                else:
                    return "NO"
            elif n >= r:
                if c[1] == None and math.gcd(r, n) > 1:
                    bst[r] = (c[0], n)
                    bst[n]=(None,None)
                    break
                elif c[1] != None:
                    r = c[1]
                else:
                    return "NO"
            else:
                return "NO"

    return "YES"


n = int(input())
tree = list(map(int, input().split()))
print(isBST(tree))
