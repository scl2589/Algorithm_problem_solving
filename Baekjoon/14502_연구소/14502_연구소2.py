N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dfs(area):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    stack = list()
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if area[i][j] == 2:
                stack.append((i,j))

    while len(stack):
        cr, cc = stack.pop()
        visited[cr][cc] = 1
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and area[nr][nc] == 0:
                area[nr][nc] = 2
                stack.append((nr, nc))

def comb(arr, idx, cnt): #1차원 배열의 조합을 구하기 위한 함수
    if cnt == 3: #모든 경우의 수를 구했으니, 더 이상 진행할 필요 없음
        #원래 보드에 벽을 세우면 안되니까 새로운 보드에 벽을 세운다.
        #tmpboard = board.copy() 얕은 복사이기 때문에 안됨 >> 깊은 복사 필요
        tmpboard = list()
        for b in board:
            #tmpboard.append([l for l in b])
            tmplist=list()
            for e in b:
                tmplist.append(e)
            tmpboard.append(tmplist)

        for i in range(len(arr)):
            if arr[i] == 1:
                r = i // M
                c = i % M
                tmpboard[r][c] = 1
        # 반복문이 끝이 나면 임의의 세개의 벽을 세운 상황
        # 바이러스 퍼뜨리기 (dfs로 진행할 수 있는 모든 빈 칸에 바이러스 만들기)
        dfs(tmp_board)

        #남아 있는 칸의 개수 세기
        remain = 0
        for i in range(N):
            for j in range(M):
                if tmp_board[i][j] == 0:
                    remain += 1
        if remain > max_area:
            max_area = remain
        return

    if idx == len(arr): #세 개를 고르지 못하고, 마지막 인덱스까지 모두 검사함
        return
    #위 2가지 경우에 부합하지 않는다면, 아직 세 위치를 정하지 못한 것이다. 다음으로 진행
    #이번 인덱스의 요소를 사용할지 안할지를 결정해서 다음 단계로 진행
    #경우의 수를 줄여 줍시다!
    tmpr = idx // M
    tmpc = idx % M
    if arr[tmpr][tmpc] == 0:
        arr[idx] = 1
        comb(arr, idx+1, cnt+1)
    #아래는 인덱스의 요소를 사용하지 않는다고 결정
    arr[idx] = 0
    comb(arr, idx+1, cnt)


#조합을 구해서 해당 조합이 의미하는 칸에 벽을 세운다
arr = [0] * (N*M)
max_area = 0
comb(arr, 0, 0)
print(max_area)