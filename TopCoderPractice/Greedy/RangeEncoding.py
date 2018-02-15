class RangeEncoding:
    def minRanges(self, arr):
        l = len(arr)
        if l == 1:
            return 1
        a = list(arr)
        ranges = 0
        i = 0
        while i < len(a):
            if i + 1 < len(a):
                if a[i + 1] != a[i] + 1:
                    print(a[i])
                    ranges += 1
            i += 1

        if l >= 2 and a[-1] != a[-2]:
            ranges += 1
        return ranges


arr = {2}
print(RangeEncoding().minRanges(arr))
