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
        elif not gettingPairs:  # getting template
            temp = ["".join([line.strip()[i], c])
                    for i, c in enumerate(line.strip()[1::])]
            polymer = Counter(temp)
            count = Counter(line.strip())
        else:  # getting insertions
            key, val = line.strip().split(' -> ')
            insertions["".join((key[0], key[1]))] = val

# print(polymer)
# print(insertions)

def insert(polymer):
    newPolymer = Counter()
    for pair, n in polymer.items():
        match = insertions.get(pair, False)  # check if pair has a match
        # print(pair, n)
        if match:  # this insertion pair occurs 'n' times in the current polymer
            count.update({match: n})
            # print(f"match: {match}, {count[match]}")
            newPair1 = "".join([pair[0], match])
            newPolymer.update({newPair1: n})

            newPair2 = "".join([match, pair[1]])
            newPolymer.update({newPair2: n})
        else:
            newPolymer.update({pair: n})
    return Counter(newPolymer)

for step in range(40):
    polymer = insert(polymer)
print(f"After step {step+1}: {polymer.keys()}")

# print(f"Template: {polymer.items()}")
occurence= count.most_common()
# print(Counter(count))
# print(polymer)
print(f"{occurence[0][1]} - {occurence[-1][1]} = {occurence[0][1] - occurence[-1][1]}")
