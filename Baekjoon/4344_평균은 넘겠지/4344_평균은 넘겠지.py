C = int(input())
for _ in range(C):
    arr = list(map(int, input().split()))
    N = arr[0]
    arr = arr[1:]
    average = sum(arr)/N
    count = 0
    for i in arr:
        if i > average:
            count += 1
    print('%.3f' % (count/N*100) + "%")