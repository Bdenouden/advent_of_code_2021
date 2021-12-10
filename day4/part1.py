import sys

class Board:
    boards = []
    def __init__(self, num) -> None:
        Board.boards.append(self)
        self.numbers = num
        self.marked = {}
        self.lastMarked = {}

    def findNum(self, num):
        result = self.numbers.get(num,False)
        if(result):
            self.markNum(num)
        return result

    def markNum(self, num):
        d = self.numbers[num]
        d['c'] = True
        self.marked[(d['x'], d['y'])] = num
        

    def hasWon(self,num):
        foundNum = self.findNum(num)
        if(not foundNum):
            return False        
        xsum = 0
        ysum = 0

        for x2 in range(0, 5):
            if(self.marked.get((x2,foundNum['y']), False)):
                xsum += 1
        for y2 in range(0,5):
            if(self.marked.get((foundNum['x'],y2), False)):
                ysum += 1
            # check if all vertical and horizontal rows for this number are checked
        return (xsum == 5) or (ysum == 5)
    
    def getUnmarkedSum(self):
        return sum([int(k) for k in self.numbers.keys() if not self.numbers[k]["c"]])
    


numList = []

with open(sys.path[0] + '/input.txt') as f:
    temp = f.read().split('\n\n')
    numList = temp[0].split(',')
    temp = temp[1:]
    for board in temp:
        d = dict()
        for y, b in enumerate(board.split("\n")):
            for x, num in enumerate([n for n in b.split(" ") if len(n)>0]):
                d[num] = {'x': x, 'y': y, 'c':False}
        Board(d)
        # print(d.keys())
        
for num in numList: 
    for b in Board.boards:
        # print(f"number {num} is found: {b.findNum(num)}")
        # print(f"Board has won: {b.hasWon(num)}")
        if(b.hasWon(num)):
            print(num)
            sum = b.getUnmarkedSum()
            print(sum)
            print(int(num)*sum)
            exit()
