c, e, m = [int(a) for a in input().split()]


sol = False
for x in range(int(e/2)-1):
    y = int(e/2) - x
    if x * y == m:
        print(x+2, y+2, flush=True)
        sol = True

if not sol:
    print("impossible", flush=True)
