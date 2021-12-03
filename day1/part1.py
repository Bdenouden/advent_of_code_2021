import sys

count = 0
lastVal = None

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        val = int(line)
        if(lastVal != None and val > lastVal):
            count+=1
        lastVal = val
print(count)
            
        