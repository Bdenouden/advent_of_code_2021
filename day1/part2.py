import sys
from collections import deque

count = 0
Q = deque([],3)
prevSum = None

with open(sys.path[0] + '/input.txt') as f:
    for i, line in enumerate(f):
        val = int(line)
        prevSum = sum(Q)
        Q.append(val)
        s = sum(Q)

        if(i >= 3 and s > prevSum):
            count +=1
        # print(f"{prevSum}\t{s}\t{'increased' if s>prevSum and i>=3 else ''}")
print(count)
            
        