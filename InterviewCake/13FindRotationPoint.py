def find_rotation_point(words):
    start = 0
    end = len(words) - 1
    pivot = words[0]
    while start <= end:
        mid = int((start + end) / 2)
        if words[mid] < pivot and start == end:
            return mid
        if words[mid] < pivot:
            end = mid
        else:
            start = mid + 1
    return 0


words = [
    'asymptote',
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage'
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist'
]
print(find_rotation_point(words))
