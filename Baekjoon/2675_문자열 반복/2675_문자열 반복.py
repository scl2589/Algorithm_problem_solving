for tc in range(int(input())):
    variable = list(input())
    mult = int(variable[0])
    for i in range(2, len(variable)):
        print(variable[i] * mult, end='')
    print('')