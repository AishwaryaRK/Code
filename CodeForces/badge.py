def get_twice_badged_student(n, students_claims):
    students = []
    for i in range(1, n + 1):
        t = {}
        s = i
        while s not in t:
            t[s] = 1
            s = students_claims[s - 1]
        students.append(s)
    return students


n = int(input())
students_claims = list(map(int, input().split()))
students = get_twice_badged_student(n, students_claims)
print(*students)
