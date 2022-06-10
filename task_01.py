# программа на диапазоне чисел от 15000000 до 25000000
# находит все простые числа сумма цифр которых кратна 13
simple = []
odd13 = []
for s in range(15000000, 25000000):
    x = 0
    for j in range(s):
        if s%(j+1)==0:
            x = x+1
        if x>=3:
            break
    if x == 2:
        simple.append(s)
print(simple)
for i in simple:
    g = 0
    f = i
    for y in range(i):
        g = g+f%10
        f = f//10
        if f<0:
            break
    if g%13==0:
        odd13.append(i)
print(odd13)
