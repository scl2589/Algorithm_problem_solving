def dfs(depth, probability):
    global answer
    if probability <= answer:
        return
    if depth == N:
        answer = max(answer, probability)
        return
    for i in range(N):
        if not check[i]:
            check[i] = True
            dfs(depth+1, probability * arr[depth][i] * 0.01)
            check[i] = False

import sys
sys.stdin = open('input.txt')

T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [False] * N
    answer = 0
    dfs(0, 100)
    print('#{} {:.6f}'.format(tc, answer))