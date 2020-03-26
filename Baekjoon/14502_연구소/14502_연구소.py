'''
연구소에 벽을 3개 세워서 바이러스를 최대한 덜 퍼트리고, 안전 영역의 최대 크기를 구하는 문제다. N*M은 최대 64이므로, 벽을 두는 모든 경우의 수를 구해서 최대 크기를 확인해 볼 수 있다.

우선 입력으로 받은 맵에 벽을 3개 세워야 한다.
벽(1)은 빈 칸(0)에만 세울 수 있다. N*M을 순회하면서 빈 칸이라면 벽을 둔다.
벽을 두는 함수는 재귀로 구현한다. 벽 카운트를 세면서 3이 되면, DFS를 통해 빈 칸에 바이러스(2)를 퍼트린다.
바이러스를 퍼트리면서, 바이러스가 퍼진 칸을 센다.
바이러스 칸이 최소가 될 때, 안전 영역의 크기가 최대가 된다.

'''
from copy import deepcopy
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

maxV= 0
virustList=list()

def count():
    count = 0
    for i in range(N): 
        for j in range(M):
            if arr[i][j] == 0:
                count += 1

def spread(i, j, copied_arr):
    if copied_arr[i][j]==2:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj <M and copied_arr[ni][nj]==0:
                copied_arr[ni][nj]=2
                spread(i, j, copied_arr)

def dfs(n, start):
    global maxV
    if n == 3:
        copied_arr=deepcopy(arr)
        for i in range(N):
            for j in range(M):
                spread(i, j, copied_arr)
        safe_count = sum(i.count(0) for i in copied_arr)
        maxV = max(maxV, safe_count)
        return True
        
    for i in range(start, N*M):
        x = i// M 
        y = i % M
        if arr[x][y]==0:
            arr[x][y] = 1
            dfs(n+1, i)
            arr[x][y] = 0 


dfs(0, 0)
print(maxV)