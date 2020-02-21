n, m, y, x, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
#동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
dice = [0, 0, 0, 0, 0, 0, 0] #6번이 밑수다
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]
for i in command:
    if x+ dx[i] < 0 or x+dx[i] >= m  or y+dy[i]< 0 or y+dy[i] >=n:
        continue
    else:
        x = x + dx[i]
        y = y + dy[i]
        if i == 1: #동쪽
            save = dice[6]
            dice[6] = dice[3]
            dice[3] = dice[1]
            dice[1] = dice[4]
            dice[4] = save

            if arr[y][x] == 0:
                arr[y][x] = dice[6]
            else:
                dice[6] = arr[y][x]
                arr[y][x] = 0
            print(dice[1])
        elif i == 2:
            save = dice[6]
            dice[6] = dice[4]
            dice[4] = dice[1]
            dice[1] = dice[3]
            dice[3] = save

            if arr[y][x] == 0:
                arr[y][x] = dice[6]
            else:
                dice[6] = arr[y][x]
                arr[y][x] = 0
            print(dice[1])
        elif i == 3:

             save = dice[6]
             dice[6] = dice[2]
             dice[2] = dice[1]
             dice[1] = dice[5]
             dice[5] = save
             if arr[y][x] == 0:
                 arr[y][x] = dice[6]
             else:
                 dice[6] = arr[y][x]
                 arr[y][x] = 0
             print(dice[1])
        elif i == 4:
            save = dice[6]
            dice[6] = dice[5]
            dice[5] = dice[1]
            dice[1] = dice[2]
            dice[2] = save
            if arr[y][x] == 0:
                arr[y][x] = dice[6]
            else:
                dice[6] = arr[y][x]
                arr[y][x] = 0
            print(dice[1])