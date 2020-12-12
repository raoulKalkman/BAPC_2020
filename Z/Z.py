import random

n = int(input())
set = []
while n > 0:
    n -= 1
    set.append(int(input()))

def sorted(a):
    return all([a[i] <= a[i+1] for i in range(len(a)-1)]) or all([a[i] >= a[i+1] for i in range(len(a)-1)])

if len(set) > 2 and not all([set[i] == set[i+1] for i in range(len(set)-1)]):
    while sorted(set):
        random.shuffle(set)

    for item in set:
        print(item, flush=True)
else:
    print('reject', flush=True)
