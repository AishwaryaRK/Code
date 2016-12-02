from pprint import pprint


class MillionGazillion:
    def __init__(self):
        self.visited = {}

    def addUrl(self, url):
        if self.isVisisted(url):
            return
        trieTraversal = self.visited
        for c in url:
            if c not in trieTraversal:
                trieTraversal[c] = {}
            trieTraversal = trieTraversal[c]
        trieTraversal['*'] = True

    def isVisisted(self, url):
        url += "*"
        trieTraversal = self.visited
        for c in url:
            if c not in trieTraversal:
                return False
            trieTraversal = trieTraversal[c]
        return True


millionGazillion = MillionGazillion()
millionGazillion.addUrl("www.google.com")
millionGazillion.addUrl("www.google1.com")
print millionGazillion.isVisisted("www.google1.com")
print millionGazillion.isVisisted("www.googsdhgcle.com")
pprint(millionGazillion.visited)
