#문자열 버전
def find(i, j, n, s):
    if n == 7:
        t.add(s)
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 4 and 0 <= nj < 4:
                find(ni, nj, n + 1, s + str(a[i][j]))

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    a = [list(map(int, input().split())) for i in range(4)]
    t = set()
    for i in range(4):
        for j in range(4):
            find(i, j, 0, '')
    print('#{} {}'.format(tc, len(t)))

