def check_string_decomposable_into_dictionary_words(dict, s):
    is_decomposable = [[False] * len(s) for i in range(0, len(s))]

    for i in range(1, len(s) + 1):
        j = 0
        while j + i <= len(s):
            a = s[j:j + i]
            if a in dict:
                is_decomposable[j][j + i - 1] = True
            else:
                k = j + 1
                while k <= j + i - 1:
                    a = s[j:k]
                    b = s[k:j + i]
                    if (a in dict or is_decomposable[j][k - 1]) and (
                            b in dict or is_decomposable[k][j + i - 1]):
                        is_decomposable[j][j + i - 1] = True
                        break
                    k += 1
            j += 1
    print(is_decomposable)
    return is_decomposable[0][-1]


print(check_string_decomposable_into_dictionary_words(['a', 'am', 'i', 'ace'], 'iamace'))
print(check_string_decomposable_into_dictionary_words(['a', 'man', 'plan', 'canal'], 'amanaplanacanal'))
print(check_string_decomposable_into_dictionary_words(['bed', 'bat', 'bath', 'beyond', 'hand', 'and'],
                                                      'bedbathandbeyond'))
