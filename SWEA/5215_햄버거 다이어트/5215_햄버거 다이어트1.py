def f(index, total_calories, score):
    global max_score

    if total_calories > L:
        return

    if index == N:
        if total_calories <= L and max_score <score:
            max_score = score
        return

    f(index + 1, total_calories, score)
    f(index + 1, total_calories+table[index][1], score + table[index][0])


T = int(input())
for tc in range(1, T+1):
    #재료의 수, 칼로리
    N, L = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    f(0, 0, 0)
    print('#{} {}'.format(tc, max_score))


