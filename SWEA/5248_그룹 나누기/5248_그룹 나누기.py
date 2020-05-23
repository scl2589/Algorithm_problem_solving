def f(n):
    stack = [n]
    while stack:
        n = stack.pop()
        if not visited[n]:
            visited[n] = 1
            stack.extend(arr[n])

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    arr = [[] for _ in range(N+1)]
    adjacent = []
    visited = [0 for _ in range(N+1)]
    # 인접
    for i in range(0, len(temp), 2):
        arr[temp[i]].append(temp[i+1])
        arr[temp[i+1]].append(temp[i])
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            f(i)
            cnt += 1
    print(f'#{tc} {cnt}')
            

