import sys

caves = {
    # start: {
    #       isBig: False,
    #       connected: set(a, b)
    # }
}
routes = []


def walk(caveName, visited=[]):
    visited.append(caveName)
    if caveName == 'end':
        routes.append(visited)
        # print('end reached!')
        return
    options = [n for n in caves[caveName]['connected'] if (caves[n]['isBig'] or (not caves[n]['isBig'] and n not in visited))]
    # print(f"current cave: {caveName}, options: {options}")
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

[print(r) for r in routes]
print(len(routes))