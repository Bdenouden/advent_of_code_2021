import sys

dumbos = {
    # (x, y): energy
}
flashes = 0


def printMatrix():
    [print("".join([str(dumbos.get((x, y), "")) for x in range(10)])) for y in range(10) if dumbos.get((0,y), -1) >=0]


def increaseAllEnergyByOne():
    flash = []
    for key in dumbos:
        if dumbos[key] == 9:
            flash.append(key)
            dumbos[key] = 0
        else:
            dumbos[key] += 1
    return flash

def ripple(flash):
    additionalFlashes=[]
    global flashes
    for x,y in flash:
        for key in [(x2, y2) for x2 in range(x-1, x+2) for y2 in range(y-1, y+2) if ((x2, y2) != (x,y))]:
            dumbo = dumbos.get(key, False)
            if(dumbo and dumbo > 0):
                if dumbos[key] == 9:
                    dumbos[key] = 0
                    additionalFlashes.append(key)
                else: 
                    dumbos[key] += 1
    if(additionalFlashes):
        flashes += len(additionalFlashes)
        ripple(additionalFlashes)    

with open(sys.path[0] + '/input.txt') as f:
    for y, line in enumerate(f):
        for x, val in enumerate(line.strip()):
            dumbos[(x, y)] = int(val)




# printMatrix()
for step in range(100):
    flash = increaseAllEnergyByOne()
    flashes += len(flash)
    ripple(flash)
    # print()
    # print(f"after step {step+1}:")
    # printMatrix()
print( flashes)