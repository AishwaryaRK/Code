def time_taken_for_trips(N, trip_times):
    trip_times.sort()
    if N * trip_times[0] <= trip_times[1]:
        return N * trip_times[0]

    t = N * trip_times[0]
    i = 0
    temp = [0] * len(trip_times)
    temp[0] = N
    while temp[0] > 0:
        if i + 1 < len(trip_times):
            i += 1
        else:
            break
        if (temp[i] + 1) * trip_times[i] <= t:
            temp[i] += 1
            temp[0] -= 1
            time1 = t - trip_times[0]
            time2 = temp[i] * trip_times[i]
            t = max(time1,time2)
            i = 0

    return t


N, K = map(int, input().split(' '))
trip_times = list()
for i in range(0, K):
    trip_times.append(int(input()))
print(time_taken_for_trips(N, trip_times))
