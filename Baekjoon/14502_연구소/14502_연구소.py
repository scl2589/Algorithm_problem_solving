N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def count():
    count = 0
    for i in range(N): 
        for j in range(M):
            if arr[i][j] == 0:
                count += 1

def spread():
    for i in range(N):
        for j in range(M):
            if arr[i][j]==2:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0<=ni<N and 0<=nj <M and arr[i][j]==0:
                        arr[ni][nj]=2

def dfs(n, k):
    if n == k:
        spread()
        return
        
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0:
                arr[i][j] = 1
                dfs(n+1, k)
                arr[i][j] = 0
                dfs(n, k)



dfs(0, 3)