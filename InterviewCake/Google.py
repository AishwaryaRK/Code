# def minimum_candies_to_buy(employee_performance_scores):
#     minimum_candies_to_buy = len(employee_performance_scores)
#     # for i in range(0, len(employee_performance_scores) - 1):
#     #     if employee_performance_scores[i] > employee_performance_scores[i + 1]:
#     #         minimum_candies_to_buy += 1
#     minimum_candies_to_buy += sum(1 for i in range(0, len(employee_performance_scores) - 1) if
#                                   employee_performance_scores[i] > employee_performance_scores[i + 1])
#     return minimum_candies_to_buy
#
#
# print(minimum_candies_to_buy([2, 5, 9, 7, 2, 3]))



def minimum_number_of_elements_to_remove(A, X):
    minimum_number_of_elements_to_remove = len(A)
    # convert the numbers in set A into binary format reversed string
    binary_A = [bin(number)[2:][::-1] for number in A]
    # convert the X into binary format reversed string
    binary_X = bin(X)[2:][::-1]
    print(binary_A)
    print(binary_X)
    print("--------")
    for i, bit in enumerate(binary_X):
        s = ''.join(map(lambda x: x[i] if len(x) > i else '0', binary_A))
        print(s)
        if s.count(bit) < minimum_number_of_elements_to_remove:
            minimum_number_of_elements_to_remove = s.count(bit)
    return minimum_number_of_elements_to_remove


# print("ans=" + str(minimum_number_of_elements_to_remove([2, 5, 9, 7, 2, 3], 15)))
print("ans=" + str(minimum_number_of_elements_to_remove([1,2,4,7], 3)))
