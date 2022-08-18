answer = ''
result = 0
steps = 0
number = 0
ogmax = 1000
max = ogmax
min = 0
while result != 1:
    steps = steps + 1
    print('Меньше', max, '?')
    answer = input()
    if answer == 'нет' and max == ogmax:
        print('Загадано:', ogmax)
        result = 1
        break
    elif answer == 'да':
        if (max//2)>min:
            max = max//2
        else:
            max = min
        # print(max)
    elif answer == 'нет' and max != ogmax:
        min = max
        print('Загадано:', max, '?')
        answer = input()
        if answer=='да':
            print('Шаги:', steps)
            break
        elif answer=='нет':
            max = max+(max//2)
