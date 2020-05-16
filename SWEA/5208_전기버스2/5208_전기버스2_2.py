def backtrack(idx, battery, cnt):
    global N, minV
    if cnt >= minV:
        return
    if idx + battery >= N:
        minV = cnt
        return
    for j in range(idx+1, idx+battery+1):
        backtrack(j, l[j], cnt+1)



T = int(input())
for tc in range(1, T+1):
    l = list(map(int, input().split()))
    N = l[0] # 정류장의 개수
    batteries = l[1:]
    minV = 100000000
    backtrack(1, batteries[0], 0)
    print('#{} {}'.format(tc, minV))