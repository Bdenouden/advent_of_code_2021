import sys


dots = []
folds = []
with open(sys.path[0] + '/input.txt') as f:
    readingCoordinates = True
    for line in f:
        if(line == '\n'):
            readingCoordinates = False
        elif(readingCoordinates):
            x, y = (int(val) for val in line.strip().split(','))
            dots.append((x, y))
        else:  # reading instructions
            temp = line.strip().split('=')
            folds.append({'axis': temp[0][-1], 'line': int(temp[1])})


def foldUp(line):
    newDots = set()
    for x, y in dots:
        if(y > line):
            newDots.add((x, abs(y-2*line)))
        else:
            newDots.add((x, y))
    return list(newDots)

def foldLeft(line):
    newDots = set()
    for x, y in dots:
        if(x < line):
            pass
            newDots.add((line + abs(line-x), y)) # TODO
            #  line + abs(5-x)
        else:
            newDots.add((x, y))
    return list(newDots)


def printGrid(dots):
    maxX, maxY = 0, 0
    for x, y in dots:
        maxX = x if x > maxX else maxX
        maxY = y if y > maxY else maxY
    grid = [['.' for _ in range(maxX + 1)] for _ in range(maxY+1)]
    for x, y in dots:
        grid[y][x] = '#'
    [print(line) for line in grid]


# printGrid(dots)
# for fold in folds:
fold=folds[0]
print(fold)
if fold['axis'] == 'y':
    dots = foldUp(fold['line'])
else:
    dots = foldLeft(fold['line'])
# print('------------------------------')
# printGrid(dots)

# printGrid(dots)
# print(dots)
print(len(dots))
