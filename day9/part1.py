import sys

hmap = {} # (x, y): value
lowPoints={}

with open(sys.path[0] + '/input.txt') as f:
    for y, line in enumerate(f):
        for x, h in enumerate(line.strip()):
            h = int(h)
            hmap[(x, y)] = {"height": h, "checked": False}
        sizeX = len(line.strip())
    sizeY = y

# print(sizeX, sizeY)

# if the check starts at 0,0 each node only needs to check x+1 and y+1 and then 
# proceed until a low point is found or a previously checked point

def findLowPoint(x,y):
    # print(f"checking x,y {x},{y}; value:{hmap[(x, y)]['height']}")
    node = hmap.get((x,y), False)
    if(not node or node['checked']): # this node has been checked, no action required
        # print("skipping!\n")
        return
    else:
        node['checked'] = True
        isLowPoint = True
        for x2 in [x-1, x+1]:
            newNode = hmap.get((x2,y), False)
            if(newNode and newNode['height'] <= node['height']):
                isLowPoint = False
                findLowPoint(x2, y)

        for y2 in [y-1, y+1]:
            newNode = hmap.get((x,y2), False)
            if(newNode and newNode['height'] <= node['height']):
                isLowPoint = False
                findLowPoint(x, y2)

        if(isLowPoint):
            print(f"-- LOWPOINT -- x, y, h = {x}, {y}, {node['height']}")
            lowPoints[(x,y)] = node['height']

        # print()

for y in range(0, sizeY-1):
    for x in range(0, sizeX-1):
        # print(x,y)
        if(not hmap[(x, y)]['checked']):
            findLowPoint(x,y)

# [print(p) for p in lowPoints.items()]  
print(len(lowPoints))   
risks = [val+1 for key, val in lowPoints.items()]
print(f"risk sum: {sum(risks)}")     