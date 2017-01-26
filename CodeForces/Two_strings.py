def get_subsequence(str1, str2):
    index = 0
    l = len(str1)
    valid_strs = []
    valid_str = ""
    invalid_strs = []
    invalid_str = ""
    for c in str2:
        i = str1.find(c, index, l)
        if i != -1:
            if invalid_str != "":
                invalid_strs.append(invalid_str)
                invalid_str = ""
            valid_str += c
            index = i + 1
        else:
            if valid_str != "":
                valid_strs.append(valid_str)
                valid_str = ""
            invalid_str += c
    if valid_str != "":
        valid_strs.append(valid_str)
    if invalid_str != "":
        invalid_strs.append(invalid_str)
    valid_strs = sorted(valid_strs, key=lambda valid_str: len(valid_str), reverse=True)
    if len(valid_strs) == 0:
        return "-"
    if len(valid_strs) == 2 and len(invalid_strs) == 1 and valid_strs[0] + invalid_strs[0] + valid_strs[1] == str2:
        return valid_strs[0] + valid_strs[1]
    return valid_strs[0]


str1 = raw_input()
str2 = raw_input()
print get_subsequence(str1, str2)
