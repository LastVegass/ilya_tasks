# Программа должна создавать объект класса машина
# машина будет обладать массой, мощностью двигателя в л.с.,
# маркой, стоимостью в долларах США, годом выпуска и
# страной производства, при создании объекта класса потребуется
# только марка машины, далее пользователь самостоятельно вводит
# всю ирформацию через функцию

class Car():

    def __init__(self, brand):
        self.brand = brand
        self.features = []

    def carInfo(self):
        for i in range(5):
            self.features.append(input())

x = Car("toyota")
print(x.brand,x.features)
x.carInfo()
print(x.brand,x.features)
