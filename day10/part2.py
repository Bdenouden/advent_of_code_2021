import sys


def check(line: str):
    while(line.find("()") + line.find("<>") + line.find("{}") + line.find("[]") > -4):
        for str in ['()', '{}', '[]', '<>']:
            line = line.replace(str, "")

    for str in ["}", "]", ")", ">"]:
        if(str in line):
            return False
    return line


def complete(line: str):
    points = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    score = 0

    for c in line[::-1]:
        score = score*5 + points[c]
    return score


with open(sys.path[0] + '/input.txt') as f:
    scores = []
    for line in f:
        result = check(line.strip())
        if(result):
            scores.append(complete(result))
    scores.sort()
    print(scores[int(len(scores)/2)])