import sys
sys.stdin = open('input.txt')
from copy import deepcopy


def top_rotate(arr): 
    #공기청정기 위쪽 구역 (반시계)
    #위쪽줄
    saved = arr[0][0]
    for x in range(C-1):
        arr[0][x]=arr[0][x+1]

    #왼쪽 세로줄
    for y in range(purifier_i-1, 0, -1):
        arr[y][0] = arr[y-1][0]
    arr[purifier_i][0] = -1 #공기청정기 위치이다.
    arr[1][0] = saved

    #아랫줄
    saved2= arr[purifier_i][C-1]
    for x in range(C-1, 1, -1):
        arr[purifier_i][x] = arr[purifier_i][x-1]
    arr[purifier_i][1] = 0

    #오른쪽 세로줄
    for y in range(purifier_i):
        arr[y][C-1] = arr[y+1][C-1]
    arr[purifier_i-1][C-1] = saved2

    #공기청정기 아래쪽 구역 (시계)
    #위쪽줄
    saved = arr[purifier_i + 1][C - 1]
    for x in range(C-1, 0, -1):
        arr[purifier_i+1][x]=arr[purifier_i+1][x-1]
    arr[purifier_i+1][1] = 0

    # 오른쪽 세로줄
    saved2 = arr[R-1][C-1]
    for y in range(R-1, purifier_i+1, -1):
        arr[y][C - 1] = arr[y - 1][C - 1]
    arr[purifier_i + 2][C - 1] = saved

    #아랫줄
    saved3 = arr[R-1][0]
    for x in range(C-1):
        arr[R-1][x] = arr[R-1][x+1]
    arr[R-1][C-2] = saved2


    #왼쪽 세로줄
    for y in range(purifier_i+1, R-1):
        arr[y][0] = arr[y+1][0]
    arr[R-2][0] = saved3
    arr[purifier_i+1][0] = -1 #공기청정기 위치 reset

    return arr


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

trial = int(input())
for tc in range(1, trial+1):
    R, C, T = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(R)]
    copied_room = deepcopy(room)

    #공기 청정기 위쪽 위치 파악
    for i in range(R):
        if room[i][0] == -1:
            purifier_i = i
            break

    for _ in range(T):
        room = deepcopy(copied_room)
        copied_room = deepcopy(room)
        #미세먼지 확산 구간
        for i in range(R):
            for j in range(C):
                if room[i][j] != -1 and room[i][j] != 0:
                    cnt = 0
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < R and 0 <= ny < C:
                            if room[nx][ny] != -1:
                                copied_room[nx][ny] += room[i][j]//5
                                cnt += 1
                    copied_room[i][j] -= ((room[i][j]//5) * cnt)

        #공기청정기 작동 구간
        room = top_rotate(copied_room)

        total = 0

        for i in range(R):
            for j in range(C):
                if room[i][j]!=0 and room[i][j]!=-1:
                    total += room[i][j]

    print(total)