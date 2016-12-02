import string


class ChessFloor:
    def minimumChanges(self, floor):
        colors = []
        for row in floor:
            colors.extend([tileColor for tileColor in row])
        colors = set(colors)
        if len(colors) == 1:
            colors = list(string.lowercase)
        minCount = len(floor) * len(floor)
        for color1 in colors:
            for color2 in colors:
                if color1 != color2:
                    count = self.calcChanges(floor, color1, color2)
                    if count <= minCount:
                        minCount = count
        return minCount

    def calcChanges(self, floor, color1, color2):
        count = 0
        for index1, row in enumerate(floor):
            for index2, tile in enumerate(row):
                if (index1 + index2) % 2 == 0 and tile != color1:
                    count += 1
                if (index1 + index2) % 2 != 0 and tile != color2:
                    count += 1
        return count


print ChessFloor().minimumChanges(
    ("jecjxsengslsmeijrmcx", "tcfyhumjcvgkafhhffed", "icmgxrlalmhnwwdhqerc", "xzrhzbgjgabanfxgabed",
     "fpcooilmwqixfagfojjq", "xzrzztidmchxrvrsszii", "swnwnrchxujxsknuqdkg", "rnvzvcxrukeidojlakcy",
     "kbagitjdrxawtnykrivw", "towgkjctgelhpomvywyb", "ucgqrhqntqvncargnhhv", "mhvwsgvfqgfxktzobetn",
     "fabxcmzbbyblxxmjcaib", "wpiwnrdqdixharhjeqwt", "xfgulejzvfgvkkuyngdn", "kedsalkounuaudmyqggb",
     "gvleogefcsxfkyiraabn", "tssjsmhzozbcsqqbebqw", "ksbfjoirwlmnoyyqpbvm", "phzsdodppzfjjmzocnge"))
