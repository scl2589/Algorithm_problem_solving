#dfs 코드
def DFS(n, v):
    if C[n][v] :
        return
    C[n][v] = 1
    if n == N:
        return
    else:
        DFS(n+1,v)
        DFS(n+1,v+D[n])
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    D = tuple(map(int,input().split()))
    s = sum(D)
    C = [[0]*(s+1) for _ in range(N+1)]
    DFS(0,0)  
    print('#{} {}'.format(tc, sum(C[N])))