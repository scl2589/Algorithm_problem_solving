def find(r, c, s):
    global minV
    if r==N-1 and c == N-1 : #목적지 도착
        if minV > s + arr[r][c]:
            minV = s + arr[r][c] #이동을 중단하고 다른 경로로 가면 시간을 줄일 수 있다.
    elif minV <= s:
        return
    else:
        if r+1<N: #아래쪽으로 이동 
            find(r+1, c, s+arr[r][c])
        if c+1<N: #오른쪽으로 이동
            find(r, c+1, s+arr[r][c])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = float('inf')
    find(0, 0, 0)
    print('#{} {}'.format(tc, minV))
