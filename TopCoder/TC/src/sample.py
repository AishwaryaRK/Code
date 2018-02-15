# def reverse(word):
#     last_letter = word[-1]
#     second_last_letter = word[-2]
#     return last_letter + " " + second_last_letter
#
#
# print(reverse("HACK"))

# from operator import itemgetter
#
#
# def sort(arr):
#     number_frequency = {}
#     for number in arr:
#         frequency = number_frequency.get(number, 0)
#         number_frequency[number] = frequency + 1
#     sorted_number_frequency = sorted(number_frequency.items(), key=itemgetter(1))
#     for number, frequency in sorted_number_frequency:
#         print(number)
#
#
# a = [8] * 1000000
# b = [9] * 100000
# c = [5] * 1000
# d = [4] * 1000000
# from itertools import chain
#
# z = list(chain.from_iterable([a, b, c]))
# sort(z)


# def is_bst(arr):
#     if len(arr) <= 1:
#         return True
#     root = arr[0]
#     left_sub_tree = []
#     right_sub_tree = []
#     index = len(arr)
#     for i in range(1, len(arr)):
#         if arr[i] <= root:
#             left_sub_tree.append(arr[i])
#         else:
#             index = i
#             break
#     for i in range(index, len(arr)):
#         if arr[i] > root:
#             right_sub_tree.append(arr[i])
#         else:
#             return False
#     is_left_bst = is_bst(left_sub_tree)
#     is_right_bst = is_bst(right_sub_tree)
#     return is_left_bst and is_right_bst
#
#
# test_cases = input()
# for _ in range(int(test_cases)):
#     input()
#     preorder_traversal = [int(n) for n in input().split(" ")]
#     print(is_bst(preorder_traversal))




# def braces(values):
#     res = []
#     for value in values:
#         braces = []
#         map = {'}': '{', ')': '(', ']': '['}
#         unbalanced = False
#         for b in value:
#             if b in ['{', '(', '[']:
#                 braces.append(b)
#             else:
#                 if len(braces) > 0 and braces[-1] == map[b]:
#                     braces.pop(-1)
#                 else:
#                     unbalanced = True
#                     break
#         if len(braces) > 0:
#             unbalanced = True
#         res.append('NO') if unbalanced else res.append('YES')
#     return res


# print(braces(["{{[(]}}","{}"]))


# def get_one_bits(n):
#     binary_n = "{0:b}".format(n)
#     count = 0
#     ans = [0]
#     for i, bit in enumerate(binary_n):
#         if bit == '1':
#             count += 1
#             ans.append(i+1)
#     ans[0]=count
#     return ans
#
# print(get_one_bits(161))


def longestEvenWord(sentence):
    words = sentence.split(" ")
    ans = ""
    for word in words:
        if len(word) > len(ans) and len(word) % 2 == 0:
            ans = word
    return ans if ans != "" else "00"

print(longestEvenWord("teh even is pleasant nnnnnnnnnn"))