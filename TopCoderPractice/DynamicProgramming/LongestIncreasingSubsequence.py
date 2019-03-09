def longest_increasing_subsequence(sequence):
    cnt = [1] * len(sequence)
    max_cnt = 1
    for i in range(1, len(sequence)):
        for j in range(0, i):
            if sequence[i] > sequence[j] and cnt[j] + 1 > cnt[i]:
                cnt[i] = cnt[j] + 1
                if cnt[i] > max_cnt:
                    max_cnt = cnt[i]
    return max_cnt

print(longest_increasing_subsequence([16, 3, 5, 19, 10, 14, 12, 0, 15]))