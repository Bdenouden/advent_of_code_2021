import sys

with open(sys.path[0] + '/input.txt') as f:
    positions = [int(c) for c in f.readline().strip().split(',')]
# print(positions)

occurence = {i:positions.count(i) for i in positions}   
# [print(occ) for occ in occurence.items()]
# bestPosition = max(occurence, key=occurence.get)
# print(bestPosition)
fuels={}
for p in positions:
    fuel=0
    for key,val in occurence.items():
        fuel += val*abs(p - key)
    fuels[p] = fuel
# print(fuels)
print(fuels[min(fuels, key=fuels.get)]) 