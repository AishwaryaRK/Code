from pprint import pprint

def get_permutations(str):
    if len(str) == 1:
        return str
    permutations = []
    for i, c in enumerate(str):
        sub_permutations = get_permutations(str[0:i] + str[i + 1:])
        for s in sub_permutations:
            permutations.append(c + s)
    return permutations


pprint(get_permutations("cats"))
