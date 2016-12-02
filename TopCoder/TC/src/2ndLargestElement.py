def second_largest_element(a):
    largest_element = a[0]
    second_largest_element = None
    for element in a:
        if element > largest_element:
            second_largest_element = largest_element
            largest_element = element
        elif element != largest_element and (
                second_largest_element == None or element > second_largest_element):
            second_largest_element = element
    return second_largest_element


a = [55, 55, -55, 55, 55]
print(second_largest_element(a))
