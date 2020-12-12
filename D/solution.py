w, h = [int(a) for a in input().split()]

points = []
for x in range(1, w+1):
    if len(points) == 2:
        break
    lim = [1, h]
    while lim[0] <= lim[1]:
        mid = int((lim[0] + lim[1]) / 2)
        print('?', x, mid, flush=True)
        res = input()
        if res == 'sea': # too low
            lim[0] = mid+1
        elif res == 'sky': # too high
            lim[1] = mid-1
        else:
            points.append((x, mid))
            break

print('!', points[0][0], points[0][1], points[1][0], points[1][1], flush=True)
