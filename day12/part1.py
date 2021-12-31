import sys

caves = {
    # start: {
    #       isBig: True,
    #       connected: set(a, b, c)
    # }
}

with open(sys.path[0] + '/test.txt') as f:
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

[print(c) for c in caves.items()]
        