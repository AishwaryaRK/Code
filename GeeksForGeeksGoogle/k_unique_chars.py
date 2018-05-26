# from operator import itemgetter
#
#
# def longest_k_unique_chars_substr(s, k):
#     positions = []
#     char_indices = {}
#     for i, c in enumerate(s):
#         if c in char_indices:
#             index = char_indices[c]
#             positions[index] = (positions[index][0], i)
#         else:
#             index = len(positions)
#             char_indices[c] = index
#             positions.append((i, i))
#
#     max_len = -1
#     i = 0
#     while i + k <= len(positions):
#         print("iter---------->", i)
#         in_start = min(positions[i: i + k], key=itemgetter(0))[0]
#         if i > 0:
#             out_left_end = max(positions[:i], key=itemgetter(1))[1]
#             if out_left_end > in_start:
#                 in_start = out_left_end + 1
#         in_end = max(positions[i: i + k], key=itemgetter(1))[1]
#         if i + k < len(positions):
#             out_right_start = min(positions[i + k:], key=itemgetter(0))[0]
#             if out_right_start < in_end:
#                 in_end = out_right_start - 1
#         print("* ",in_start,in_end,in_end - in_start + 1)
#         if (in_end - in_start + 1) > max_len:
#             max_len = in_end - in_start + 1
#         i += 1
#
#     print(positions)
#     return max_len

import collections


def longest_k_unique_chars_substr(s, k):
    start = 0
    max_len = 0
    i = 0
    while i < len(s):
        while len(collections.Counter(s[start:i])) < k:
            i += 1


# t = int(input())
# for i in range(0, t):
#     s = input()
#     k = int(input())
#     print(longest_k_unique_chars_substr(s, k))

print(len("whsqmgbbuqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqca"))
print(longest_k_unique_chars_substr("whsqmgbbuqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqca", 5))
