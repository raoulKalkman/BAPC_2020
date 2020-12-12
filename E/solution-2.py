h, w = [int(a) for a in input().split()]
map = [[int(a) for a in input().split()] for i in range(h)]

def traverse(map, c):
    x, y = c
    prev = int(map[y][x])
    if prev <= 1:
        return
    map[y][x] = -1 # label

    for t in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        x2 = x + t[0]
        y2 = y + t[1]
        if 0 <= y2 < h and 0 <= x2 < w:
            if map[y2][x2] > 0:
                traverse(map, (x2, y2))


areas = 0
for x in range(w):
    for y in range(h):
        if map[y][x] > 1: # New area
            traverse(map, (x, y))
            areas += 1
print(areas)
