class Pronunciation:
    def canPronounce(self, words):
        vowels = ['a', 'e', 'i', 'o', 'u']
        for word1 in words:
            word = word1.lower()
            for i, w in enumerate(word):
                if w in vowels:
                    if i + 1 < len(word):
                        if word[i + 1] in vowels and word[i + 1] != w:
                            return word1
                elif i + 2 < len(word):
                    if word[i + 1] not in vowels and word[i + 2] not in vowels:
                        return word1
        return ""


print(Pronunciation().canPronounce(["Aa"]))
