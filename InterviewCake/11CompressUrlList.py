from pprint import pprint

trie = {}


def is_visited(url):
    ptr = trie
    is_visited = True
    for c in url:
        if c in ptr:
            ptr = ptr[c]
        else:
            ptr[c] = {}
            ptr = ptr[c]
            is_visited = False
    if not is_visited:
        ptr['*'] = {}
    pprint(trie)
    return is_visited


print(is_visited("www.google.com"))
print(is_visited("www.google.com"))
