def move(i, j, total):
    global minV
    if total > minV:
        return
    if i == N-1:
        minV = min(minV, total + arr[j][0])
        return
    for k in range(1, N):
        if not visited[k]:
            visited[k] = 1
            move(i+1, k, total + arr[j][k])
            visited[k]=0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = float('inf')
    route = []
    visited = [0] * N
    move(0, 0, 0)
    print('#{} {}'.format(tc, minV))