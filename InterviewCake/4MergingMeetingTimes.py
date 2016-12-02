from operator import itemgetter

def condense_meeting_times(meeting_time_ranges):
    meeting_time_ranges = sorted(meeting_time_ranges, key=itemgetter(0, 1))
    condensed_meeting_time_ranges = []
    for i in iter(range(0, len(meeting_time_ranges) - 1)):
        if meeting_time_ranges[i + 1][0] <= meeting_time_ranges[i][1]:
            condensed_meeting_time_ranges.append(
                (meeting_time_ranges[i][0], max(meeting_time_ranges[i][1], meeting_time_ranges[i + 1][1])))
            # i=i+1
        else:
            condensed_meeting_time_ranges.append(meeting_time_ranges[i])
    return condensed_meeting_time_ranges


print(condense_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
