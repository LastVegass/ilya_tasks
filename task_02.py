# пользователь вводит любое целое число, программа создает
# квадратичную матрицу с количеством строк и столбцов равному
# этому числу, программа заполняет матрицу случайными числами
# от 10 до 99

from random import randint
number = int(input("Number "))
for g in range(number):
    part = []
    for h in range(number):
        part.append(randint(10, 99))
    print(part)
