class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        root = self.trie
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
        if None not in root:
            root[None] = None

    def search(self, word):
        root = self.trie
        for c in word:
            if c not in root:
                return False
            root = root[c]
        if None not in root:
            return False
        return True

    def startsWith(self, prefix):
        root = self.trie
        for c in prefix:
            if c not in root:
                return False
            root = root[c]
        return True


t = Trie()
t.insert("apple")
print(t.trie)
print(t.search("apple"))
print(t.startsWith("appq"))
