def is_word_break_possible(dictionary, s):
    d = dictionary
    for c in s:
        if c in d:
            d = d[c]
            if None in d:
                d = dictionary
        else:
            return 0
    return 1


def create_trie(d):
    dictionary = {}
    for word in d:
        dict = dictionary
        for c in word:
            if c not in dict:
                dict[c] = {}
            dict = dict[c]
        dict[None] = None
    return dictionary


t = int(input())
for i in range(0, t):
    n = int(input())
    dictionary = input().strip().split(' ')
    s = input()
    print(is_word_break_possible(dictionary,s))


# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# dictionary = "i like sam sung samsung mobile ice cream icecream man go mango".split(' ')
# dictionary = create_trie(dictionary)
# pp.pprint(dictionary)
# s = "ilike"
# print(is_word_break_possible(dictionary, s))
