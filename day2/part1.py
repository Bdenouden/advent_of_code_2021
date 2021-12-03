import sys

pos = {
    "x": 0,
    "d":0
}

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        instr, step = line.split(" ")
        step=int(step)
        # print(f"{instr}\t{step}")
        if(instr == "forward"):
            pos["x"] += step
        elif(instr == "down"):
            pos["d"] += step
        elif(instr == "up"):
            pos["d"] -= step
        
print(f'{pos["x"]} * {pos["d"]}\t= {pos["d"]*pos["x"]}')