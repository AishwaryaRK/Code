class TextCompressor:
    def longestRepeat(self, sourceText):
        max_sub_str = ""
        l = len(sourceText)
        for i, c in enumerate(sourceText):
            j = sourceText.find(c, i + 1, l)
            if j != -1:
                t = ""
                start = j
                while i < l and j < l and i < start:
                    if sourceText[i] != sourceText[j]:
                        break
                    else:
                        t += sourceText[i]
                        i += 1
                        j += 1
                if len(t) > len(max_sub_str):
                    max_sub_str = t
        return max_sub_str


print(TextCompressor().longestRepeat("ABABA"))
