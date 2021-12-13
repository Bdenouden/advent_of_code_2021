import sys

hmap = {} # (x, y): value
lowPoints={}

with open(sys.path[0] + '/test.txt') as f:
    for y, line in enumerate(f):
        for x, h in enumerate(line.strip()):
            h = int(h)
            hmap[(x, y)] = {"height": h, "checked": False}
        sizeX = len(line.strip())
    sizeY = y

print(sizeX, sizeY)

# if the check starts at 0,0 each node only needs to check x+1 and y+1 and then 
# proceed until a low point is found or a previously checked point

def findLowPoint(x,y):
    print(f"checking x,y {x},{y}; value:{hmap[(x, y)]['height']}")
    if hmap[(x, y)]['checked']: # this node has been checked, no action required
        return False 
    else:
        hmap[(x, y)]['checked'] = True
        valSelf = hmap[(x, y)]['height']
        valRight = hmap[(x+1, y)]['height']
        valBelow = hmap[(x, min(sizeY-1, y+1))]['height']
        print(f"valSelf={valSelf}, valRight={valRight}, valBelow={valBelow}")

        if (valRight < valSelf and valRight < valBelow ):
            return findLowPoint(min(x+1, sizeX-2), y) #check value to right
        elif(valBelow < valSelf):
            return  findLowPoint(x, min(sizeY-1, y+1)) # check value below
        elif(lowPoints.get((x-1, y), False) or lowPoints.get((x, y-1), False)): # check if no lower point has already be found to the left
            return False
        else:
            print(f"LowPoint found: x,y {x},{y}; value:{valSelf}")
            lowPoints[(x, y)]=valSelf
            hmap[(x+1, y)]['checked'] = True
            hmap[(x, y+1)]['checked'] = True
            hmap[(max(0,x-1), y)]['checked'] = True
            hmap[(x, max(0,y-1))]['checked'] = True
            return True



def test(x,y):
    for y2 in [max(0, y-1), min(y+1, sizeY-1)]:
        if y != y2:
            pass # check if xy is larger than x2y2
        
    for x2 in [max(0, x-1), min(x+1, sizeX-1)]:
        if x != x2:
            pass #check if xy is larger than x2y2








for y in range(0, sizeY-1):
    for x in range(0, sizeX-1):
        print(x,y)
        if(not hmap[(x, y)]['checked']):
            findLowPoint(x,y)

[print(p) for p in lowPoints.items()]