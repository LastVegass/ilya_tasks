class Car():
    def __init__(self, brand):
            self.brand = brand
            self.features = {'weight': [],
                             'power': [],
                             'cost': [],
                             'year': [],
                             'country': []
                            }

    def carInfo(self, weight, power, cost, year, country):
        self.features['weight'].append(weight)
        self.features['power'].append(power)
        self.features['cost'].append(cost)
        self.features['year'].append(year)
        self.features['country'].append(country)

    def changeFtr(self, feature, changedvalue):
            self.features[feature].clear()
            self.features[feature].append(changedvalue)

x = Car("toyota")
x.carInfo(100, 100, 10000, 1997, 'Sweden')
print(x.features)
x.changeFtr('weight', 34)
x.changeFtr('year', 2000)
print(x.features)
