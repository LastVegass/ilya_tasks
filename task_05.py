answer = ''
result = 0
steps = 0
number = 0
ogmax = 1000
max = ogmax
while result != 1:
    steps = steps + 1
    print('Меньше', max, '?')
    answer = input()
    if answer == 'нет' and max == ogmax:
        print('Загадано:', ogmax)
        result = 1
        break
    elif answer == 'да':
        max = max//2
        # print(max)
    elif answer == 'нет' and max != ogmax:
        steps = steps + 1
        print('Загадано:', max, '?')
        answer = input()
        if answer=='да':
            print('Шаги:', steps)
        elif answer=='нет':
            max = max+(max//2)
