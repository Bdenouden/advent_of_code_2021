import sys

hmap = {}  # (x, y): value
lowPoints = {}
visited = {}

with open(sys.path[0] + '/input.txt') as f:
    for y, line in enumerate(f):
        for x, h in enumerate(line.strip()):
            h = int(h)
            hmap[(x, y)] = {"height": h, "checked": False}
        sizeX = len(line.strip())
    sizeY = y


def findLowPoint(x, y):
    node = hmap.get((x, y), False)
    if(not node or node['checked']):  # this node has been checked, no action required
        return
    else:
        node['checked'] = True
        isLowPoint = True
        for x2 in [x-1, x+1]:
            newNode = hmap.get((x2, y), False)
            if(newNode and newNode['height'] <= node['height']):
                isLowPoint = False
                findLowPoint(x2, y)

        for y2 in [y-1, y+1]:
            newNode = hmap.get((x, y2), False)
            if(newNode and newNode['height'] <= node['height']):
                isLowPoint = False
                findLowPoint(x, y2)

        if(isLowPoint):
            # print(f"-- LOWPOINT -- x, y = ({x}, {y}), height = {node['height']}")
            lowPoints[(x, y)] = node['height']


def findBasin(x, y, visited, depth=0):
    node = hmap.get((x, y), False)
    if(not node or visited.get((x,y), False)):
        return
    # print('| '*depth+f"- findBasin; x: {x}, y: {y}, height: {node['height']} ")
    visited[(x, y)] = node['height']
    for x2, y2 in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        nextNode = hmap.get((x2, y2), False)
        if(nextNode and nextNode['height'] < 9):
            # print("| "*(depth+1) + f'ping ({x2}, {y2}, {nextNode["height"]})')
            findBasin(x2, y2, visited, depth=depth+1)
    #     else:
    #         print("| "*(depth+1) + f'---- ({x2}, {y2}, {hmap[(x2, y2)]["height"] if hmap.get((x2,y2), False) else False })')
    # print("| "*(depth+1) + f"returning {visited}")
    # print("| "*(depth))
    return visited


for y in range(0, sizeY-1):
    for x in range(0, sizeX-1):
        if(not hmap[(x, y)]['checked']):
            findLowPoint(x, y)


risks = [val+1 for key, val in lowPoints.items()]
print(f"risk sum: {sum(risks)}")

basins = [findBasin(x, y, dict()) for (x, y) in lowPoints]
# [print(b) for b in basins]
basinSizes = [len(b) for b in basins]
basinSizes.sort(reverse=True)
# print(basinSizes)
print(basinSizes[0]*basinSizes[1]*basinSizes[2])
