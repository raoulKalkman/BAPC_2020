w, h = [int(a) for a in input().split()]    #h = height, w = width

#for x-axis binary search -> find either horizon or 2 pixels where sky > sea
# (recursive)
#   with found horizon (can be float) look at pixels y, y+1, y-1, y+2, y-2,.... -> check if horizon is found here
#   when valid horizon pixel is found (not float) store in points
#   when points has 2 points -> return

points = []
column = [] #for x axis
for x in range(1, w+1):
    if len(points) == 2:
        break
    lim = [1, h]
    while lim[0] <= lim[1]:
        mid = int((lim[0] + lim[1]) / 2)
        print('?', x, mid, flush=True)
        res = input() #get input for mid
        column[mid] = res

        if res == 'sea': # too low
            if column[mid + 1] == 'sky': #horizon between mid & mid + 1


            lim[0] = mid+1
        elif res == 'sky': # too high
            if column[mid - 1] == 'sea':



            lim[1] = mid-1
        else:
            points.append((x, mid))
            break

print('!', points[0][0], points[0][1], points[1][0], points[1][1], flush=True)
