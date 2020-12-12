# Assignment: given a map of different buildings of different hights, find how many elevators makes all available

# Solution: make an elevator at the highest point in the map, check which tiles are reachable at each hight > 1

h, w = [int(a) for a in input.split()]
map = [[int(a) for a in input().split()] for i in range(h)]
