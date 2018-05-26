class SearchBox:
    def find(self, text, search, wholeWord, start):
        i = start
        index = -1
        while i < len(text):
            if text[i] == search[0]:
                index = i
                flag = True
                for j, s in enumerate(search):
                    if text[i + j] != s:
                        flag = False
                        break
                if flag:
                    if wholeWord == "Y":
                        if index != 0 and text[index - 1] != " ":
                            return -1
                        if index + len(search) < len(text) and text[index + len(search)] != " ":
                            return -1
                    return index
            i += 1
        return -1


print(SearchBox().find("All in all youre just another brick in the wall",
                       "just",
                       "Y",
                       17))
