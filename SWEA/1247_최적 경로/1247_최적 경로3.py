# 윤지언니 코드
# 최적경로
def f(x, y, cnt, s):
    global minV
    if minV <= s:
        return
    if cnt == N+1:
        i, j = x, y
        temp = abs(i-hx)+abs(j-hy)
        if minV > temp+s:
            minV = temp+s
            return
    j, k = x, y
    for i in range(N):
        if not v[i]:
            v[i] = 1
            a, b = dxy[i]
            temp = abs(j-a)+abs(k-b)
            f(a, b, cnt+1, temp+s)
            v[i] = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = list(map(int, input().split()))
    cx = d.pop(0)
    cy = d.pop(0)
    hx = d.pop(0)
    hy = d.pop(0)
    dxy = []
    v = [0]*(N)
    for i in range(0, N*2, 2):
        dxy.append((d[i], d[i+1]))
    minV = float('inf')
    f(cx, cy, 1, 0)
    print(f'#{tc} {minV}')