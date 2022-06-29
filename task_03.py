# Программа должна создавать объект класса машина
# машина будет обладать массой, мощностью двигателя в л.с.,
# маркой, стоимостью в долларах США, годом выпуска и
# страной производства, при создании объекта класса потребуется
# только марка машины, далее пользователь самостоятельно вводит
# # всю ирформацию через функцию
#
class Car():
    def __init__(self, brand):
            self.brand = brand
            self.features = {'weight': [],
                             'power': [],
                             'cost': [],
                             'year': [],
                             'country': []
                            }

    def carInfo(self, weight, power, cost, year, nation):
        for k,v in self.features.items():
            self.features[k].append(input('Please input '))

    def changeFtr(self):
        feature = input('Which feature to change: ')
        if feature!='weight' or feature!='power' or feature!='cost' or feature!='year' or feature!='country':
            print('ERROR: Given feature does not exist')
        else:
            changedvalue = input('New value: ')
            self.features[feature].clear()
            self.features[feature].append(changedvalue)

x = Car("toyota")
print(x.brand,x.features)
x.carInfo(100, 100, 10000, 1997, 'Sweden')
print(x.features)
print(type(x.features['weight']))
x.changeFtr()
print(x.features['weight'])
print(x.features)
