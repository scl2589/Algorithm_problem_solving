def recursion(i, j, sum):
    global minV
    if sum > minV:
        return
    if i == N-1 and j == N-1:
        if sum < minV:
            minV = sum
        return
    for k in range(2):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            	recursion(ni, nj, sum+arr[ni][nj])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = float('inf')
    recursion(0, 0, arr[0][0])
    print('#{} {}'.format(tc, minV))