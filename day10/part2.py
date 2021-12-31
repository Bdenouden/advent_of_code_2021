import sys

def check(line:str):
    # print(line)
    while(line.find("()") + line.find("<>") + line.find("{}") + line.find("[]") > -4):
        for str in ['()', '{}', '[]','<>']:
            line = line.replace(str, "")  
    # print(line)

    for str in ["}", "]", ")", ">"]:
        if(str in line):
            return False
    return True


with open(sys.path[0] + '/test.txt') as f:
    for i, line in enumerate(f):
        print(check(line.strip()))
