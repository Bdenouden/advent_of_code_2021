import sys
numDays = 256

with open(sys.path[0] + '/input.txt') as f:
    school = [int(f) for f in f.readline().strip().split(',')]

fishType = [school.count(f) for f in range(9)] # countdown 0, 1, 2, 3, 4, 5, 6, 7, 8
for day in range(numDays): # number of days
    fishSpawning = fishType[0]
    fishType = [fishType[i+1] for i in range(8)]
    fishType.append(fishSpawning)
    fishType[6]+= fishSpawning
    
print(sum(fishType))