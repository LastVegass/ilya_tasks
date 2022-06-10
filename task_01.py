# программа на диапазоне чисел от 15000000 до 25000000
# находит все простые числа сумма цифр которых кратна 13
numbers = []
for s in range(15000000, 25000000):
    x = 0
    for j in range(s):
        if s%(j+1)==0:
            x = x+1
        if x>=3:
            break
    if x==2:
        numbers.append(s)
print(numbers)
