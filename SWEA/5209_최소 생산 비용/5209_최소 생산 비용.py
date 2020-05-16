def f(n, k, s):
    global minV
    if n == k:
        minV = min(s, minV)
        return
    elif minV <= s:
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                f(n+1, k, s+prod_cost[n][i])
                visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    prod_cost = [list(map(int, input().split())) for _ in range(N)]
    minV = float('inf')
    visited = [0] * N
    f(0, N, 0)
    print(f"#{tc} {minV}")