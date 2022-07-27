# создать класс LandscapeMap, объект класса должен представлять собой
# карту, представленную матрицей заданных размером, которая будет
# заполнять каждую ячейку случайным объектом ландшафта, горы, реки,
# поля и тд., далее объет класса просто выводится в терминал

from random import randint
class LandscapeMap():

    def __init__(self, ver, hor):
        self.map = []
        self.ver = ver
        self.hor = hor

    def makeMap(self):
        for i in range(self.ver):
            part = []
            for g in range(self.hor):
                ls = randint(1, 7)
                if ls == 1:
                    part.append('R')
                elif ls == 2:
                    part.append('L')
                elif ls == 3:
                    part.append('P')
                elif ls == 4:
                    part.append('M')
                elif ls == 5:
                    part.append('F')
                elif ls == 6:
                    part.append('W')
                elif ls == 7:
                    part.append('S')
            self.map.append(part)

    def showMap(self):
        for j in self.map:
            print(j)

    def buildRoad(self):
        for part in self.map:
            count = 0
            for g in part:
                type = g
                if type == 'P' or type == 'F' or type == 'W':
                    part[count] = '*'
                count = count + 1

    def buildBridge(self):
        hcount = 0
        vcount = 0
        for part in self.map:
            if vcount == 5:
                break
            else:
                for g in part:
                    type = g
                    if hcount == 0 or hcount == len(part)-1  or vcount==0 or vcount==len(part)-1:
                        continue
                    if type == 'R' or type == 'L':
                        if self.map[vcount-1]=='*' and self.map[vcount+1]=='*':
                            part[hcount] == '|'
                        elif self.map[hcount-1]=='*' and self.map[hcount+1]=='*':
                            part[hcount] == '='
                    if hcount != 4:
                        hcount = hcount + 1
                    else:
                        hcount = 1
                        vcount = vcount + 1

x = LandscapeMap(5, 5)
print(x.map)
x.makeMap()
print('---------------------')
x.showMap()
print('---------------------')
x.buildRoad()
x.showMap()
print('---------------------')
x.buildBridge()
x.showMap()
