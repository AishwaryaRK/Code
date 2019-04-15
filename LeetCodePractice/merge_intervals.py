class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


# merge all overlapping intervals.
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
def merge(intervals):
    if len(intervals) == 0:
        return intervals
    intervals.sort(key=lambda e: (e.start, e.end))
    print(intervals)
    min = None
    max = None
    ans = []
    for interval in intervals:
        if min == None and max == None:
            min = interval.start
            max = interval.end
        else:
            if interval.start > max:
                ans.append(Interval(min, max))
                min = interval.start
                max = interval.end
            else:
                if interval.end > max:
                    max = interval.end
    ans.append(Interval(min, max))
    return ans
