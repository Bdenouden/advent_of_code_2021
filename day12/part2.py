import sys
from collections import Counter

caves = {
    # start: {
    #       isBig: False,
    #       connected: set(a, b)
    # }
}
routes = []

def getOptions(caveName, visited):
    options = []
    count = Counter([v for v in visited if not caves[v]['isBig']]) # list all visited small caves
    doubleSmallCave = all(c < 2 for c in count.values()) # true if no small cave has previously been visited twice or more
    for option in caves[caveName]['connected']:
        if (caves[option]['isBig']): # big caves may always be visited
            options.append(option)
        elif (option not in visited): # small caves may be visited once
            options.append(option)
        elif(option not in ['start', 'end'] and doubleSmallCave ): # a single small  cave may be visited twice
            # print(f'Cave {caveName} raises double cave ping for option {option}, this claim is {"valid" if option in visited else "invalid"}')
            options.append(option)
    return options

def walk(caveName, visited=[]):
    visited.append(caveName)
    if caveName == 'end':
        routes.append(visited)
        # print(f'end reached! the chosen route is:\n{visited}\n')
        return
    options = getOptions(caveName, visited) # doublesmallcave will be set to true also if only the first option will trigger this, this causes the routefinder to miss valid paths
    # if not options:
    #     print(f"Discarding route {visited}")
    # print(f"current cave: \033[94m{caveName}\033[0m, options: {options}")
    for option in options:
        walk(option, [v for v in visited]) # make deepcopy of past route

def getData(file):
    with open(sys.path[0] + '/'+file+'.txt') as f:
        for line in f:
            nodes = line.strip().split('-')
            for cave in nodes:
                if(not caves.get(cave, False)):
                    caves[cave] = {
                        'isBig': cave.isupper(),
                        'connected': set([c for c in nodes if c != cave])
                    }
                else:
                    caves[cave]['connected'].add([c for c in nodes if c != cave][0])

getData('input')
# [print(c) for c in caves.items()]

walk('start')   

print("\nEnd of routefinding, the results are:")
# [print(",".join(r)) for r in routes]
print(len(routes))