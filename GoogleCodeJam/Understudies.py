def show_succeed_probability(N, ditch_probabilities):
    ditch_probabilities = sorted(ditch_probabilities)
    p = 1
    for i in range(0, N):
        p *= (1 - ditch_probabilities[i] * ditch_probabilities[-(i + 1)])
    return p


T = int(input())
for n in range(1, T + 1):
    N = int(input())
    ditch_probabilities = list(map(float, input().split(" ")))
    p = show_succeed_probability(N, ditch_probabilities)
    print("Case #" + str(n) + ": " + str(p))
