import sys

gridSize = 1000
grid = [[0 for _ in range(0, gridSize)] for _ in range(0, gridSize)]

def printGrid():
    for xline in grid:
        print(xline)

# take start and end coordinates as [x, y] and add 1 to all grid values it crosses
def addXLineToGrid(start, end):
    for x in range(start[0], end[0] + 1 -2*int(start[0]>end[0]), 1-2*(start[0] > end[0])):
        grid[start[1]][x] += 1

def addYLineToGrid(start, end):
    for y in range(start[1], end[1] + 1 -2*int(start[1]>end[1]), 1-2*(start[1] > end[1])):
        grid[y][start[0]] += 1

def addDLineToGrid(start, end):
    dirx = 1-2*int(start[0] > end[0])
    diry = 1-2*int(start[1] > end[1])
    x = start[0]
    y = start[1]

    while True:
        grid[y][x] += 1
        if x == end[0]:
            break
        x += dirx
        y += diry



with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        l = [[int(c) for c in xy.split(',')] for xy in line.strip().split(' -> ')] # create line array
        if(l[0][0] == l[1][0]):
            addYLineToGrid(l[0], l[1])
            pass
        elif(l[0][1] == l[1][1]):
            addXLineToGrid(l[0], l[1])
            pass
        else:
            addDLineToGrid(l[0], l[1])


count =0
for line in grid:
    for val in line:
        if(val>= 2):
            count += 1
print(count)