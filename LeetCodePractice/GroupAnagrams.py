import collections


def groupAnagrams(strs):
    hash = {}
    for s in strs:
        k = ['0'] * 26
        c = collections.Counter(s)
        for i, j in c.items():
            k[ord(i) - ord('a')] = str(j)
        k = "".join(k)

        if k not in hash:
            hash[k] = [s]
        else:
            v = hash[k]
            v.append(s)
            hash[k] = v

    return list(hash.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
