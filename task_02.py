# пользователь вводит любое целое число, программа создает
# квадратичную матрицу с количеством строк и столбцов равному
# этому числу, программа заполняет матрицу случайными числами
# от 10 до 99
from random import randint
number = int(input("Number "))
# number = 4
arr = []
for g in range(number):
    part = []
    for h in range(number):
        part.append(randint(10, 99))
    arr.append(part)
    print(part)

print('#####')
newarr = []
for i in arr:
   print(i)
indver = 0
indhor = 0
for g in arr:
    for i in g:
        if indver == 0 and indhor == 0:
            newarr.append(arr[indver][indhor+1]
                          +arr[indver+1][indhor+1]
                          +arr[indver+1][indhor]
                         )
            indhor = indhor + 1
        elif indver == 0 and indhor == number-1:
            newarr.append(arr[indver][indhor-1]
                          +arr[indver+1][indhor]
                          +arr[indver+1][indhor-1]
                         )
        elif indver == 0 and indhor>0:
            newarr.append(arr[indver][indhor-1]
                          +arr[indver+1][indhor-1]
                          +arr[indver+1][indhor]
                          +arr[indver+1][indhor+1]
                          +arr[indver][indhor+1]
                         )
            indhor = indhor +1
        elif indver > 0 and indhor == 0:
            newarr.append(arr[indver-1][indhor]
                          +arr[indver-1][indhor+1]
                          +arr[indver][indhor+1]
                          +arr[indver][indhor+1]
                          +arr[indver][indhor]
                         )
            indhor = indhor +1
        elif indver > 0 and indver < 0 and indhor > 0 and indhor < 0:
            newarr.append(arr[indver-1][indhor]
                          +arr[indver-1][indhor+1]
                          +arr[indver][indhor+1]
                          +arr[indver+1][indhor+1]
                          +arr[indver+1][indhor]
                          +arr[indver+1][indhor-1]
                          +arr[indver][indhor-1]
                          +arr[indver-1][indhor-1]
                         )
    indhor = 0
    indver = indver + 1
    print(newarr)
    newarr = []
    if indver == number:
        break

for j in newarr:
    print(j)
