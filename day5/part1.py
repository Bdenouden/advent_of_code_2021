import sys

gridSize = 1000
grid = [[0 for x in range(0, gridSize)] for y in range(0, gridSize)]

def printGrid():
    for xline in grid:
        print(xline)

# take start and end coordinates as [x, y] and add 1 to all grid values it crosses
def addXLineToGrid(start, end):
    # print(f"X start {start[0]}, end {end[0]}, step { 1-2*(start[0] > end[0])}")
    for x in range(start[0], end[0] + 1 -2*int(start[0]>end[0]), 1-2*(start[0] > end[0])):
        grid[start[1]][x] += 1

def addYLineToGrid(start, end):
    # print(f"Y start {start[1]}, end {end[1]}, step { 1-2*(start[1] > end[1])}")
    for y in range(start[1], end[1] + 1 -2*int(start[1]>end[1]), 1-2*(start[1] > end[1])):
        grid[y][start[0]] += 1

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        l = [[int(c) for c in xy.split(',')] for xy in line.strip().split(' -> ')] # create line array
        if(l[0][0] == l[1][0]):
            addYLineToGrid(l[0], l[1])
        elif(l[0][1] == l[1][1]):
            addXLineToGrid(l[0], l[1])

        # print(l)
        # print()
# printGrid()
# print()

count =0
for line in grid:
    for val in line:
        if(val>= 2):
            count += 1
print(count)