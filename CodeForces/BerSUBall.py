def get_max_pairs(n, m, boys, girls):
    boys.sort()
    girls.sort()
    people = []

    i = j = 0
    while i < n or j < m:
        a = b = None
        if i < n:
            a = boys[i]
        if j < m:
            b = girls[j]
        if a != None and b != None:
            if a < b:
                people.append(('B', a))
                i += 1
                if b - a <= 1:
                    people.append(('G', b))
                    j += 1
            elif b < a:
                people.append(('G', b))
                j += 1
                if a - b <= 1:
                    people.append(('B', a))
                    i += 1
            else:
                people.append(('B', a))
                people.append(('G', b))
                i += 1
                j += 1
        else:
            if a == None:
                people.append(('G', b))
            else:
                people.append(('B', a))
            break

    max_pairs = 0
    i = 0
    l = len(people)
    while i < l - 1:
        if people[i][0] == 'B' and people[i + 1][0] == 'G' and people[i + 1][1] - people[i][1] <= 1:
            max_pairs += 1
            i += 2
        elif people[i][0] == 'G' and people[i + 1][0] == 'B' and people[i + 1][1] - people[i][1] <= 1:
            max_pairs += 1
            i += 2
        else:
            i += 1

    return max_pairs


n = int(input())
boys = list(map(int, input().split()))
m = int(input())
girls = list(map(int, input().split()))
print(get_max_pairs(n, m, boys, girls))
