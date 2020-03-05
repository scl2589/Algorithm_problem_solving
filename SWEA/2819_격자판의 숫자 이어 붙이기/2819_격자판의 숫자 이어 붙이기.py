#내 버전
def f(i, j, index, temp):
    if index == 6:
        result.add(temp)
        return

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni <4 and 0<=nj <4:
            f(ni, nj, index+1, temp+table[ni][nj])


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    table = [list(map(str, input().split())) for _ in range(4)]
    result = set()
    for x in range(4):
        for y in range(4):
            string = table[x][y]
            f(x, y, 0, string)
    print('#{} {}'.format(tc, len(result)))


