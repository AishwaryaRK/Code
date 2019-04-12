def sort_k_messed_array(arr, k):
    if len(arr) == 0:
        return arr

    combinations = []
    for i in range(0, len(arr)):
        temp = [combination[:] for combination in combinations]
        combinations = []
        for index in range(i - k, i + k + 1):
            if i == 0 and index >= 0 and index < len(arr):
                combinations.append([arr[index]])
            else:
                for combination in temp:
                    if index >= 0 and index < len(arr) and arr[index] > combination[-1]:
                        temp_combination = combination[:]
                        temp_combination.append(arr[index])
                        combinations.append(temp_combination)

    print(combinations)
    for combination in combinations:
        if is_sorted(combination):
            return combination


def is_sorted(combination):
    for i in range(0, len(combination) - 1):
        if combination[i] >= combination[i + 1]:
            return False

    return True


print(sort_k_messed_array([1, 4, 5, 2, 3, 7, 8, 6, 10, 9], 2))
# print(sort_k_messed_array([6, 1, 4, 11, 2, 0, 3, 7, 10, 5, 8, 9], 6))
