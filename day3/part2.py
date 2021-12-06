import sys

# get all data from file
length = 12
data =[]
mostOccuringBit = None
leastOccuringBit = None

with open(sys.path[0] + '/input.txt') as f:
    ones = 0
    for i, line in enumerate(f):
        data.append(line.strip('\n'))
    moreOnes = 2*ones <= i
    mostOccuringBit = str(int(moreOnes))
    leastOccuringBit = str(int(not moreOnes))



# print(data)

oxy = f"{mostOccuringBit}"
co2 = f"{leastOccuringBit}"
# print(f"{oxy[-1]}, {co2[-1]}")
# val1 = "1"

def getBit(col, filter, param):
    oneCount = 0
    zeroCount = 0
    lastResult = {0:'', 1:''}
    # print()
    for line in data:
        if (line[0:col] == param):
            # print(f"evaluating string {line}")
            if(line[col] == '1'):
                oneCount += 1
                lastResult[1] = line
            else:
                zeroCount += 1
                lastResult[0] = line
    # print("-------------------")
    return (oneCount, zeroCount, lastResult)

def getMostOccuringBit(col, filter):
    oneCount, zeroCount, lastResult = getBit(col, filter, oxy)
    temp = oneCount >= zeroCount
    count = oneCount if temp else zeroCount
    # print(f"Most occuring: {str(int(temp))}")
    return count, lastResult[temp], str(int(temp)) 

def getLeastOccuringBit(col, filter):
    oneCount, zeroCount, lastResult = getBit(col, filter, co2)
    temp = oneCount < zeroCount
    count = zeroCount if temp else oneCount
    # print(f"Least occuring: {str(int(temp))}")
    return count, lastResult[temp], str(int(temp)) 


def getOxy():
    global oxy
    for i in range(1,length):
        numResults, result, bit = getMostOccuringBit(i, oxy[-1])
        # print(f"numresults = {numResults}")
        if(numResults == 1):
            return result
        else:
            oxy += bit

def getCo2():
    global co2
    for i in range(1,length):
        numResults, result, bit = getLeastOccuringBit(i, co2[-1])
        # print(f"numresults = {numResults}")
        if(numResults == 1):
            return result
        else:
            co2 += bit
    
oxyResult = getOxy()
co2Result = getCo2()

print(f"oxy: {oxy}, {int(oxyResult,2)},\t co2: {co2}, {int(co2Result,2)}")
print(f"solution: {int(oxyResult,2)*int(co2Result,2)}")
# print(val1)