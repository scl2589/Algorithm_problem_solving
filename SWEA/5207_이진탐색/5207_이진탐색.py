def binary(target, start, end, data, direction):
    mid = (start+end)//2
    if data[mid] == target:
        return 1
    elif data[mid] > target and direction !='left':
        return binary(target, start, mid-1, data, 'left')
    elif data[mid] < target and direction != 'right':
        return binary(target, mid+1, end, data, 'right')
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    count = 0
    for i in B:
        if binary(i, 0, len(A)-1, A, ""):
            count += 1
    print("#{} {}".format(tc, count))
