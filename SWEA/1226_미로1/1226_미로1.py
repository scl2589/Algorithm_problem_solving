def bfs(i, j):
    q = [] # 큐 생성
    q.append((i, j)) #시작점 enq
    v = [[0]*16 for _ in range(16)] #처리 표시 배열 v생성 
    v[i][j] = 1 # 시작점 처리 표시
    while q: # q가 비어있지 않으면 반복
        i, j = q.pop(0) #i, j = 디큐 (i, j칸 방문)
        if maze[i][j] == '3': # 목적지 확인, 목적지면 return 1
            return 1
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # i, j에 인접인 ni, nj를 찾으면
            ni, nj = i + di, j + dj
            if maze[ni][nj] != '1' and v[ni][nj] == 0:  #인접: 벽이 아니고 처리 전
                q.append((ni, nj)) # ni, nj 인큐 및 처리표시
                v[ni][nj] = v[i][j]+1
    return 0 # 목적지에 도착하지 못하면 리턴 0

 

def f(): #시작 위치를 찾는 함수
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                return bfs(i, j) #시작 위치부터 bfs탐색

for _ in range(1, 11):
    tc = int(input())
    maze = [input() for _ in range(16))] #[list(map(int, input())) for _ in range(16)]
    print(f'#{tc} {f()}')
