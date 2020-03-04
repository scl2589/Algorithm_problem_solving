def f(n, k, s):
    global maxV
    if n == k:
        if maxV < s:
            maxV = s
        return
    if maxV >= s:
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            f(n+1, k, s*arr[i][n]*0.01)
            visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    maxV = 0
    f(0, N, 1)
    print('#{} {:6f}'.format(tc, maxV*100))

