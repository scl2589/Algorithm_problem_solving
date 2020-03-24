R, C = map(int, input().split())
grass = [list(input()) for _ in range(R)]


def dfs(i, j):
    visited[i][j] = 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<R and 0<=nj<C and grass[ni][nj]=='#' and visited[ni][nj]==0:
            visited[ni][nj] = 1

            
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

count = 0
visited = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if grass[i][j] == '#' and not visited[i][j]:
            dfs(i, j)
            count += 1

print(count)