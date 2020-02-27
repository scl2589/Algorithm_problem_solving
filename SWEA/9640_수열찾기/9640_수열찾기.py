
def move(x, y, idx):
    if idx == target-1:
        return 1
    else:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0<= ny < M and arr[nx][ny] == numbers[idx+1]:
                arr[nx][ny]=0
                if move(nx, ny, idx+1) == 1:
                    return 1
                arr[nx][ny]=numbers[idx+1]

        return 0


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    target= numbers[0]
    numbers= numbers[1:]

    M = int(input()) #N
    arr = [list(map(int, input().split())) for _ in range(M)]

    flag = True
    for i in range(M):
        for j in range(M):
            if arr[i][j] == numbers[0]:
                if move(i, j, 0) == 1:
                    print('#{} 1'.format(tc))
                    flag = False
                    break
        if not flag:
            break

    if flag:
        print('#{} 0'.format(tc))




