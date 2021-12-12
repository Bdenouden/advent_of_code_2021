import sys

with open(sys.path[0] + '/input.txt') as f:
    positions = [int(c) for c in f.readline().strip().split(',')]
occurence = {i:positions.count(i) for i in positions}   

def weirdSum(n):
    return sum([i for i in range(n+1)])

fuels={}
for p in occurence.keys():
    fuel=0
    for key,val in occurence.items():
        fuel += val*weirdSum(abs(p - key))
    fuels[p] = fuel
print(fuels[min(fuels, key=fuels.get)]) 
