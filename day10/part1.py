import sys

points = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137,
}

def check(line:str):
    # print(line)
    while(line.find("()") + line.find("<>") + line.find("{}") + line.find("[]") > -4):
        for str in ['()', '{}', '[]','<>']:
            line = line.replace(str, "")  
    # print(line)
    for c in line:
        if c in points.keys():
            return points[c]
    return 0


with open(sys.path[0] + '/input.txt') as f:
    totalPoints = 0
    for line in f:
        totalPoints += check(line.strip())
    print(totalPoints)