for tc in range(1, int(input()) + 1):
    W, H, N = map(int, input().split())
    x, y = map(int, input().split())  # x1, y1

    ans = 0
    for _ in range(N - 1):  # N-1 개의 좌표를 입력받는다.
        tx, ty = map(int, input().split())
        a = x - tx
        b = y - ty
        if a * b < 0:
            ans += abs(a) + abs(b)
        else:
            ans += max(abs(a), abs(b))
        x , y = tx, ty

    print('#{} {}'.format(tc, ans))