h, w = [int(a) for a in input().split()]
map = [[int(a) for a in input().split()] for i in range(h)]

def find_max(map, c):
    x, y = c
    b = []
    l = []
    for t in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        x2 = x + t[0]
        y2 = y + t[1]
        if 0 <= y2 < h and 0 <= x2 < w:
            if map[y2][x2] >= map[y][x]:
                res = traverse(map, (x2, y2))
                if res:
                    b.append(map[res[0]][res[1]])
                    l.append(res)
    if b:
        return l[b.index(max(b))]
    return c

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
            if map[y2][x2] > 0 and map[y2][x2] <= prev:
                traverse(map, (x2, y2))


areas = 0
for x in range(w):
    for y in range(h):
        if map[y][x] > 1: # New area
            m = find_max(map, (x, y))
            traverse(map, m)
            areas += 1
print(areas)
