#시간초과..
def f(total_calories, score):
    global max_score

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            if total_calories + table[i][1] <= L:
                f(total_calories + table[i][1], score +table[i][0])
            else:
                if max_score < score:
                    max_score = score
                visited[i] = 0
                return
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    #재료의 수, 칼로리
    N, L = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_score = 0
    f(0, 0)
    print('#{} {}'.format(tc, max_score))


