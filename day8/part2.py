import sys


def decode(decoder, message):
    return int("".join([str(decoder[s]) for s in message]))

total=0
with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        input, output = line.strip().split(' | ')
        input = sorted(["".join(sorted(c)) for c in input.split(' ')], key=len)
        output = ["".join(sorted(c)) for c in output.split(' ')]
        nums={
            1: input[0],
            4: input[2],
            7: input[1],
            8: input[9]
        }        
        for n in input[3:9]:
            if(len(n)==6):
                if (set(n + nums[7])==set(nums[8])): # find nr 6 by equating segmentes used for 6+7 == 8
                    nums[6] = n
                elif(len(set(n).difference(set(nums[4] + nums[7]))) == 1):
                    nums[9] = n
                else:
                    nums[0] = n
            else: # len == 5
                if(len(set(n).difference(set(nums[7])))==2 ):
                    nums[3] = n
                elif(len(set(n).difference(set(nums[4])))==2):
                    nums[5] = n
                else:
                    nums[2]=n
        outputVal = decode({ v:k for k,v in nums.items()}, output)
        total += outputVal
        print(f"output {output}: {outputVal}")
        # print(sorted(nums.items()))
print(total)