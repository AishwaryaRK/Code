from pprint import pprint

def condense_meeting_times(meetingTimes):
    meetingTimes=sorted(meetingTimes);
    previousStartTime, previousEndTime = meetingTimes[0]
    condense_meeting_times = []
    for currentStartTime, currentEndTime in meetingTimes[1:]:
        if previousEndTime >= currentStartTime:
            previousEndTime = max(previousEndTime, currentEndTime)
        else:
            condense_meeting_times.append((previousStartTime, previousEndTime))
            previousStartTime = currentStartTime
            previousEndTime = currentEndTime

    condense_meeting_times.append((previousStartTime, previousEndTime))
    return condense_meeting_times


pprint(condense_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))