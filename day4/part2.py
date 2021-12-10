import sys

class Board:
    boards = []
    def __init__(self, num) -> None:
        Board.boards.append(self)
        self.id = len(Board.boards)
        self.numbers = num
        self.marked = {}

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

            # check if all vertical and horizontal rows for this number are checked
        for x in range(0, 5):
            if(self.marked.get((x,foundNum['y']), None) is not None):
                xsum += 1
        for y in range(0,5):
            if(self.marked.get((foundNum['x'],y), None) is not None):
                ysum += 1
        return (xsum >= 5) or (ysum >= 5)
    
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

for num in numList: 
    for b in [b for b in Board.boards]:
        if(b.hasWon(num)):
            Board.boards.remove(b)
            if(len(Board.boards) == 0 ): 
                print(num)
                sum = b.getUnmarkedSum()
                print(sum)
                print(int(num)*sum)
                exit()
    
