import sys
from collections import Counter

# approach:
# polymer template is a list
# insertions are a dict for fast lookup
# loop over the list and find n and n+1 as a kay for the insertions dict


polymer = []
insertions = {}
with open(sys.path[0] + '/input.txt') as f:
    gettingPairs = False
    for line in f:
        if line == '\n':
            gettingPairs = True
        elif not gettingPairs: # getting template
            polymer = line.strip()
        else:  # getting insertions
            key, val = line.strip().split(' -> ')
            insertions[(key[0], key[1])] = val

# print(polymer)
# print(insertions)

def insert(polymer):
    newPolymer = []
    for c in range(1, len(polymer)):
        newPolymer.append(polymer[c-1])
        i = insertions.get((polymer[c-1], polymer[c]), False)
        if(i): # insertion found
            newPolymer.append(i)
    newPolymer.append(polymer[-1])
    return "".join(newPolymer)


print(f"Template: {polymer}")
for step in range(10):
    polymer = insert(polymer)
    print(f"After step {step+1}: {len(polymer)}")

occurence= Counter(polymer).most_common()
print(f"{occurence[0][1]} - {occurence[-1][1]} = {occurence[0][1] - occurence[-1][1]}")