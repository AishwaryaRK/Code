import requests
import urllib
from bs4 import BeautifulSoup


class WordPuzzle:
    def getWords(self, puzzle):
        words = []
        rowLength = len(puzzle[0])
        colLength = len(puzzle);
        for i in range(0, colLength):
            for j in range(0, rowLength):
                for k in range(6, rowLength):
                    if (j + k) <= rowLength:
                        words.append(puzzle[i][j:j + k])
        for i in range(0, rowLength):
            for j in range(0, colLength):
                for k in range(6, colLength):
                    if (j + k) <= colLength:
                        words.append(''.join(map(lambda x: x[i], puzzle[j:j + k])))
        return words

    def getValidEnglishWords(self, words):
        validEnglishWords = []
        for word in words:
            res = requests.get("http://api.pearson.com/v2/dictionaries/entries?headword=" + word)
            res = res.text
            if res.count(str.lower(word)) == 1:
                print(word)
                validEnglishWords.append(word)
        return validEnglishWords


puzzle = ["INITIATIVEJBACZ",
          "MNIKJJHFXORRRHI",
          "FAVMRUMVNAIEOAJ",
          "GKDETOIEICWYELB",
          "NKEMNVWNAONVHLZ",
          "IBVSITMMPYISAES",
          "MVIDLIIMATSSYNI",
          "EITTLYEVAEDIQGG",
          "ESCLBXCVEATRSEV",
          "TIUCQROEVITAERC",
          "GODAHNPASSIONAV",
          "DNOMNALOHLQZGAX",
          "MDRIORNBUODOXOF",
          "NWPLRUGGAVYGSXL",
          "UPIMCPQPEQFEHEB"]
words = WordPuzzle().getWords(puzzle)
print(len(words))
print(words)
print(WordPuzzle().getValidEnglishWords(words))
