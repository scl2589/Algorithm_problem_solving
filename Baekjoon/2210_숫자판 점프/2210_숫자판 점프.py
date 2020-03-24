arr = [list(input().split()) for _ in range(5)]
result = set()

def dfs(i, j, index, word):
    if index == 5:
        result.add(word)
        return
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<5 and 0<=nj<5:
            dfs(ni, nj, index+1, word+arr[ni][nj])
    


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for i in range(5):
    for j in range(5):
        dfs(i, j, 0, arr[i][j])
print(len(result))