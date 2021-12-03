import sys

length = 12
values = [0]*length
gamma =[0]*length
epsilon=[0]*length

with open(sys.path[0] + '/input.txt') as f:
    for iter, line in enumerate(f):
        for i in range(0,length):
            # print(f"{i}\t{line[i]}")
            values[i] += int(line[i])
print(values, iter)     
for i in range(0, length):
    gamma[i] = str(int(values[i] > (iter/2)))
    epsilon[i] = str(int(values[i] < (iter/2)))
gamma = "".join(gamma)
epsilon = "".join(epsilon)
print(f"gamma: {gamma}, eps:{epsilon}") 

power_consumption = int(epsilon,2)*int(gamma,2)
print(power_consumption)