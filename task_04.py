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

x = LandscapeMap(10, 10)
print(x.map)
x.makeMap()
x.showMap()
