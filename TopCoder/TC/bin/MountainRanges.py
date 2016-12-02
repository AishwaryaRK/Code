class MountainRanges:
    def countPeaks(self, heights):
        if len(heights) == 1:
            return 1
        count = 0
        for i, ht in enumerate(heights):
            if i == 0:
                if heights[i] > heights[i + 1]:
                    count += 1
            elif i == len(heights) - 1:
                if heights[i] > heights[i - 1]:
                    count += 1
            elif heights[i] > heights[i + 1] and heights[i] > heights[i - 1]:
                count += 1
        return count


print(MountainRanges().countPeaks([2, 1]))
