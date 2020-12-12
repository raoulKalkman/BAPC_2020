n, p = [int(a) for a in input().split(' ')] # teams, problems - 1e4
rankings = [int(input()) for i in range(n)] # ranking, time score - 1e6

# Find how many problems each team has solved
# - 0 time penalty means that 0 problems have been solved, when a low number follows a high one a new numbers of solutions has been found

solved = [None for i in range(n)]
for i in range(n-1, -1, -1):
    if rankings[i] == 0:
        solved[i] = 0
    elif rankings[i] <= rankings[i+1]:
        solved[i] = solved[i+1]
    else:
        solved[i] = solved[i+1] + 1

if solved[0] == p:
    for s in solved:
        print(s)
else:
    print('ambiguous')
