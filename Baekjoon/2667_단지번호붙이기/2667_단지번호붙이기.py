#dfs
N = int(input())

arr = [list(input()) for _ in range(N)]
result = []
count = 0

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dfs(i, j):
    global count 
    arr[i][j] = '0'
    count += 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni <N and 0<=nj < N and arr[ni][nj]=='1':
            dfs(ni, nj)

for i in range(N):
    for j in range(N):
        if arr[i][j]=='1':
            count = 0
            dfs(i, j)
            result.append(count)

print(len(result))
for i in sorted(result):
    print(i)