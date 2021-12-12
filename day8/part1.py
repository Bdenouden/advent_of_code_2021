import sys

digits = {
    1: {'len': 2, 'options':[]},
    4: {'len': 4, 'options':[]},
    7: {'len': 3, 'options':[]},
    8: {'len': 7, 'options':[]},
}

count=0
with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        input, output = line.strip().split(' | ')
        output = [c for c in output.split(' ')]
        for str in output:
            for num, data in digits.items():
                if len(str) == data['len']:
                    data['options'].append(str)
                    count += 1

print(count)
