h, w = [int(a) for a in input().split()]
map = [[int(a) for a in input().split()] for i in range(h)]

def top(map):
    m = 0
    c = None
    for x in range(w):
        for y in range(h):
            if map[y][x] > m:
                m = map[y][x]
                c = (x, y)
    if m > 1:
        return c
    else:
        return None

def traverse(map, c):
    x, y = c
    prev = int(map[y][x])
    if prev <= 1:
        return
    map[y][x] = 1

    for t in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        x2 = x + t[0]
        y2 = y + t[1]
        if 0 <= y2 < h and 0 <= x2 < w:
            if map[y2][x2] >= 1 and prev >= map[y2][x2]:
                traverse(map, (x2, y2))



def place_elevators(map):
    used = 0
    while True:
        target = top(map)
        if target is None:
            break

        traverse(map, target)
        used += 1
    return used

print(place_elevators(map), flush=True)
