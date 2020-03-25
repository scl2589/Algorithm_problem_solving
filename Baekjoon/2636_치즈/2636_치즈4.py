#내가 푼 문제
import sys
sys.setrecursionlimit(10000)
def dfs(i, j):
    arr[i][j]=-1
    visited[i][j] = 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k] 
        if 0<=ni <N and 0<=nj<M and visited[ni][nj]==0:
            #dfs를 하면서 치즈와 인접한 부분은 0으로 변경
            if arr[ni][nj]==1:
                visited[ni][nj]=1
                melt.append([ni, nj])
            else:
                dfs(ni, nj)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
time = 0

while True:
    visited = [[0]*M for _ in range(N)]
    melt=[]
    dfs(0,0)
    if not len(melt):
        break
    time += 1
    one_hour_before=len(melt)
    while melt:
        x, y = melt.pop()
        arr[x][y] = -1
print(time)
print(one_hour_before)