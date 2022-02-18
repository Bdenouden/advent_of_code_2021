import sys

field = {}

with open(sys.path[0] + '/test.txt') as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            field[(x,y)] = char 

def searchPath(x, y):
    val = field[(x,y)]
    return val