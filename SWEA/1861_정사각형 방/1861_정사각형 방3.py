def find_num(x, y):
    for k in range(4):
        current_x = x + dx[k]
        current_y = y + dy[k]
        if 0<= current_x <N and 0<=current_y <N and arr[x][y]+1 == arr[current_x][current_y]:
            return True
    else:
        return False


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    V = [0 for _ in range(N*N)]

    for i in range(N):
        for j in range(N):
            if find_num(i, j):
                V[arr[i][j]] = 1

    cnt = 0
    max_cnt = 0
    start = 0
    for a in range(N*N-1, -1, -1):
        if V[a] == 1:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                start = i+1
            cnt = 0

    print('#{} {} {}'.format(tc, start, max_cnt+1))

