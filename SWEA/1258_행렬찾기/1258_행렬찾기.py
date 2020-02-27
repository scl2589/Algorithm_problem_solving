T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [[False] * N for _ in range(N)]

    result = []
    start_i, start_j = 0, 0
    keep_going = True

    while keep_going:
        for i in range(N):
            for j in range(N):
                if check[i][j] == False and arr[i][j] >= 1:
                    start_i = i
                    start_j = j
                    for k in range(j + 1, N):
                        if arr[i][k] == 0:
                            end_j = k - 1
                            break
                        if k == N - 1:
                            end_j = k
                            break
                    for l in range(i + 1, N):
                        if arr[l][k - 1] == 0:
                            end_i = l - 1
                            break
                        if l== N-1:
                            end_i = l
                            break
                    for a in range(start_i, end_i + 1):
                        for b in range(start_j, end_j + 1):
                            check[a][b] = True
                    result.append([end_i - start_i + 1, end_j - start_j + 1])

        if i == N - 1 and j == N - 1:
            keep_going = False

    new_result = sorted(result, key=lambda x: (x[0] * x[1], x[0]))
    print('#{} {}'.format(tc, len(new_result)), end=' ')
    for i in range(len(new_result)):
        print(new_result[i][0], new_result[i][1], end=' ')
    print()