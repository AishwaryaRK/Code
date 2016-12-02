class ListeningSongs:
    def listen(self, durations1, durations2, minutes, T):
        if len(durations1) < T or len(durations2) < T:
            return -1
        count = T * 2
        durations1 = sorted(durations1)
        durations2 = sorted(durations2)
        minutes *= 60
        for i in range(0, T, 1):
            sum = durations1[i] + durations2[i]
            if minutes >= sum:
                minutes -= sum
            else:
                return -1
        i = 0
        durations = durations1[T:]+durations2[T:]
        durations=sorted(durations)
        while minutes > 0:
            if i < len(durations) and minutes >= durations[i]:
                count += 1
                minutes -= durations[i]
                i += 1
            else:
                break
        return count


print ListeningSongs().listen((100, 200, 300, 400, 500, 600), (100, 200), 1000, 3)
