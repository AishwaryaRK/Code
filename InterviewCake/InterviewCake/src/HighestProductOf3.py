def get_highest_product_of_3(arr):
    highest1 = arr[0]
    highest2 = arr[0]
    highest3 = arr[0]
    lowest1 = arr[0]
    lowest2 = arr[0]
    lowest3 = arr[0]
    for a in arr:
        if a > highest1:
            highest3 = highest2
            highest2 = highest1
            highest1 = a
        elif a > highest2:
            highest3 = highest2
            highest2 = a
        elif a > highest3:
            highest3 = a
        elif a < lowest1:
            lowest3 = lowest2
            lowest2 = lowest1
            lowest1 = a
        elif a < lowest2:
            lowest3 = lowest2
            lowest2 = a
        elif a < lowest3:
            lowest3 = a
    print(highest1, highest2, highest3)
    print(lowest1, lowest2, lowest3)
    a = highest1 * highest2 * highest3
    b = lowest1 * lowest2 * highest1
    return a if a > b else b


print(get_highest_product_of_3([1, 10, -5, 1, -100]))
