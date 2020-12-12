n, p = [int(a) for a in input().split(' ')] # teams, problems - 1e4
rankings = [int(input()) for i in range(n)] # ranking, time score - 1e6

# Que: Find how many problems each team has solved
# Sol: 0 time penalty means that 0 problems have been solved, when a low number follows a high one a new numbers of solutions has been found (to explain the ranking)

solved = [None for i in range(n)]
for i in range(n-1, -1, -1): # Start at lowest score
    if rankings[i] == 0: # have solved zero
        solved[i] = 0
    elif rankings[i] <= rankings[i+1]: # ranked behind eachother
        solved[i] = solved[i+1]
    else: # high follows low, must be because of different ranks
        solved[i] = solved[i+1] + 1

if solved[0] == p: # Can fill the scores exactly because all numbers used
    for s in solved:
        print(s, flush=True)
else:
    print('ambiguous', flush=True)
