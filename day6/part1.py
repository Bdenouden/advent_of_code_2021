import sys

with open(sys.path[0] + '/input.txt') as f:
    school = [int(f) for f in f.readline().split(',')]
# print(school)

for i in range(0, 80):
    newSchool=[]
    for f in school:
        if (f == 0):
            newSchool.append(6)
            newSchool.append(8)
        else:
            newSchool.append(f-1)
    # print(f"Day {i} has {len(newSchool)} fish")
    school = [fish for fish in newSchool] #deepcopy
print(len(school))