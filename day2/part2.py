import sys

pos = {
    "x": 0,
    "d": 0,
    "a": 0
}

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        instr, step = line.split(" ")
        step=int(step)
        # print(f"{instr}\t{step}")
        if(instr == "forward"):
            pos["x"] += step
            pos["d"] += step * pos["a"]
        elif(instr == "down"):
            pos["a"] += step
        elif(instr == "up"):
            pos["a"] -= step
        
print(f'{pos["x"]} * {pos["d"]}\t= {pos["d"]*pos["x"]}')