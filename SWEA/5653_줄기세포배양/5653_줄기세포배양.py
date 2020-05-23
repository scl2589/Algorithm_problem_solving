def f(arr, time):
    if time == K:
        for i in range(N+K):
            for j in range(N+K):
                if arr[i][j] != 0:
                    count += 1
        return count
    else:
        for i in range(N+K):
            for j in range(N+K):
                if arr[i][j] != 0:
                    arr[i][j] -= 1
                    if arr[i][j] == 0:
                        for k in range(4):
                            ni = i + di[k]
                            nj = j + dj[k]
                            if arr[ni][nj] != 0:
                                arr[ni][nj] -= 1
                            else:
                                arr[ni][nj] = active[i][j]
                                active[ni][nj] = active[i][j]
 dx = [1, 0, 0, -1]
 dy = [0, 1, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [[0]*(N+K) for _ in range(M+K)]
    center = [list(map(int, input().split())) for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            arr[i+K//2][j+K//2] = center[i][j]

    active = [arr[i] for i in range(M+K)]
    result = f(arr)
    print(f'#{tc} {result}')