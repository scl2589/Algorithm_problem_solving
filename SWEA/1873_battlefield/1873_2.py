dx = [-1, 1, 0, 1]
dy = [0,0,-1,1]
cmd = {'U':0, 'D':1, 'L':2, 'R':3, 'S':4}
tank = '^v<>'

for tc in range(1, int(input())+1):
    W, H = map(int, input().split())
    x = y = d = 0
    MAP = [] #탱크의 위치
    for i in range(H):
        MAP.append(list(input())) #변경하기 위해
        for j in range(W):
            if  MAP[i][j] in tank:
                x, y = i, j
                d = tank.index(MAP[i][j])
    N = int(input())
    cmdStr= input()
    #명령순으로 처리
    for c in cmdStr:
        if cmd[c] ==4: #사격
            #현재 위치 x, y, 방향
            tx, ty = x+dx[d] , y + dy[d]
            while 0<=tx <H and 0<=ty <W:
                if MAP[tx][ty]  == "#":
                    break
                if MAP[tx][ty] =="*":
                    MAP[tx][ty] == ".":
                        break
                tx, ty = tx +dx[d], ty + dy[d]
        else:
            #방향을 전환한다
            # 그 방향으로 전진한다. 만약 경계 밖, 벽, 물이면 안돼
            d = cmd[c]
            MAP[x][y] = tank[d]
            tx, ty = x +dx[d], y + dy[d]
            if tx<- or tx<=H or ty<0 or ty==W: continue
            if MAP[tx][ty]=='.':
                MAP[tx][ty] = tank[d]
                MAP[x][y]='.'
                x, y = tx, ty
            