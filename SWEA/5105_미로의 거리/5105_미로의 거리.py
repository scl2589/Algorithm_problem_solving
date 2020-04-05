def bfs(i, j):
    global result
    q.append((i, j))
    visited.append((i, j))
    while q: 
        i , j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited:
                if arr[ni][nj]==0 or arr[ni][nj]==3:
                    q.append((ni, nj))
                    visited.append((ni, nj))
                    dist[ni][nj] = dist[i][j] + 1
                    if arr[ni][nj]==3:
                        result = dist[ni][nj]-1
                        return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = []
    q = []
    start_i, start_j = 0, 0

    flag = False
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_i, start_j = i, j
                flag = True
                break
        if flag:
            break
    
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    result = 0
    dist = [[0]*N for _ in range(N)]

    bfs(start_i, start_j)
    print('#{} {}'.format(tc, result))