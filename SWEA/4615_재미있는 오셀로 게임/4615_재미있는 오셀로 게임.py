dx = [-1, -1, -1, 0, 1, 1, 1, 0] #8방향 탐색을 위해 행과 열에 더해줄 값
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split()) #N: 보드판, M: 돌을 놓는 횟수
    
    # 게임판의 상태를 저장
    pan = [[0]*(N+1) for _ in range(N+1)]
    #초기 게임판의 상태를 설정
    p = N//2
    pan[p][p] = pan[p+1][p+1] = 2
    pan[p+1][p] = pan[p][p+1] = 1
    
    #M번의 돌을 놓는 정보 처리
    for _ in range(M):
        x, y, dol = map(int, input().split())
        pan[x][y] = dol
        
        for i in range(8):
            tx, ty = x + dx[i], y +dy[i]
            
            while 1 <= tx <=N and 1 <= ty <= N:
                if pan[tx][ty] == 0:
                    break
                if pan[tx][ty] == dol:
                    while tx!= x or ty!=y:
                        pan[tx][ty] = dol
                        tx, ty = tx - dx[i], ty - dy[i]
                    break
                tx, ty = tx+dx[i] , ty+dy[i]
    #pan에 저장된 1의 개수, 2의 개수를 카운팅하기
    w = 0
    b = 0
    for i in range(N+1):
        for j in range(N+1):
            if pan[i][j] == 1:
                w += 1
            elif pan[i][j] == 2:
                b += 1
    print('#{} {} {}'.format(tc, w, b))