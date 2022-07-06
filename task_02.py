from random import randint
number = int(input("Number "))
arr = []
for g in range(number):
    part = []
    for h in range(number):
        part.append(randint(10, 99))
    arr.append(part)
    print(part)

print('##################################')
newarr = []
rf = 0
indver = 0
indhor = 0
for g in arr:
    for i in g:
        if indver == 0 and indhor == 0:
            newarr.append(arr[indver][indhor+1]
                          +arr[indver+1][indhor+1]
                          +arr[indver+1][indhor]
                         )
            # print('indver', indver, '|', 'indhor', indhor)
            indhor = indhor + 1
        elif indver == 0 and indhor == number-1:
            newarr.append(arr[indver][indhor-1]
                          +arr[indver+1][indhor]
                          +arr[indver+1][indhor-1]
                         )
            # print('indver', indver, '|', 'indhor', indhor)
        elif indver == 0 and indhor>0:
            newarr.append(arr[indver][indhor-1]
                          +arr[indver+1][indhor-1]
                          +arr[indver+1][indhor]
                          +arr[indver+1][indhor+1]
                          +arr[indver][indhor+1]
                         )
            # print('indver', indver, '|', 'indhor', indhor)
            indhor = indhor +1
        elif indver == number-1 and indhor == 0:
            newarr.append(arr[indver-1][indhor]
                          +arr[indver-1][indhor+1]
                          +arr[indver][indhor+1]
                         )
            # print('indver', indver, '|', 'indhor', indhor)
            indhor = indhor + 1
        elif indver == number-1 and indhor > 0 and indhor < number-1:
            newarr.append(arr[indver][indhor-1]
                          +arr[indver-1][indhor-1]
                          +arr[indver-1][indhor]
                          +arr[indver-1][indhor+1]
                          +arr[indver][indhor+1]
                         )
            # print('indver', indver, '|', 'indhor', indhor)
            indhor = indhor + 1
        elif indver > 0 and indhor == 0:
            newarr.append(arr[indver-1][indhor]
                          +arr[indver-1][indhor+1]
                          +arr[indver][indhor+1]
                          +arr[indver+1][indhor+1]
                          +arr[indver+1][indhor]
                         )
            # print('indver', indver, '|', 'indhor', indhor)
            indhor = indhor +1
        elif indver > 0 and indhor == number-1:
            newarr.append(arr[indver-1][indhor]
                          +arr[indver-1][indhor-1]
                          +arr[indver][indhor-1]
                          +arr[indver-1][indhor-1]
                          +arr[indver-1][indhor]
                         )
            # print('indver', indver, '|', 'indhor', indhor)
        elif indver > 0 and indver and indver < number-1 and indhor > 0 and indhor < number-1:
            # rf = rf + 1
            # print(rf)
            newarr.append(arr[indver-1][indhor]
                          +arr[indver-1][indhor+1]
                          +arr[indver][indhor+1]
                          +arr[indver+1][indhor+1]
                          +arr[indver+1][indhor]
                          +arr[indver+1][indhor-1]
                          +arr[indver][indhor-1]
                          +arr[indver-1][indhor-1]
                         )
            # print('indver', indver, '|', 'indhor', indhor)
            indhor = indhor + 1

    indhor = 0
    indver = indver + 1
    print(newarr)
    newarr = []
    if indver == number:
        break

for j in newarr:
    print(j)
