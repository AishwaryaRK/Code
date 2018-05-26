def flood_fill(pixels, n, m, x, y, k, p):
    if (x * m + y) < 0 or (x * m + y) >= len(pixels):
        return pixels
    if pixels[x * m + y] != p:
        return pixels
    pixels[x * m + y] = k
    if x - 1 >= 0:
        pixels = flood_fill(pixels, n, m, x - 1, y, k, p)
    if x + 1 < n:
        pixels = flood_fill(pixels, n, m, x + 1, y, k, p)
    if y + 1 < m:
        pixels = flood_fill(pixels, n, m, x, y + 1, k, p)
    if y - 1 >= 0:
        pixels = flood_fill(pixels, n, m, x, y - 1, k, p)
    return pixels


t = int(input().strip())
for i in range(0, t):
    n, m = map(int, input().strip().split(' '))
    pixels = list(map(int, input().strip().split(' ')))
    x, y, k = map(int, input().strip().split(' '))
    pixels = flood_fill(pixels, n, m, x, y, k, pixels[x * m + y])
    print(*pixels)
