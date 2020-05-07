for tc in range(int(input())):
    arr = list(input())
    sum = 0
    count = 0
    for i in arr:
        if i == 'O':
            count += 1
            sum += count
        else:
            count = 0
    print(sum)