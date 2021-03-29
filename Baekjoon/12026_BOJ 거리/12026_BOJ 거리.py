N = int(input())
arr = input() 

MAX = float('inf')
dp = [MAX] * N 

def get_prev(x):
    if x == 'B':
        return 'J'
    elif x == 'O':
        return 'B'
    elif x == 'J':
        return 'O'

dp[0] = 0
for i in range(1, N):
    prev = get_prev(arr[i])
    for j in range(i):
        if arr[j] == prev:
            dp[i] = min(dp[i], dp[j] + (i-j)**2)

if dp[N-1] != MAX:
    print(dp[N-1])
else:
    print(-1)

# 더 빠른 코드
N = int(input())
block = list(input())

def solution(N, block):
    DP = [2000000 for _ in range(N)]
    DP[0] = 0
    for i in range(len(block)):
        start = block[i]
        for j in range(i+1, len(block)):
            end = block[j]
            if (start == 'B' and end == 'O') or (start == 'O' and end == 'J') or (start == 'J' and end == 'B'):
                DP[j] = min(DP[i]+(j-i)*(j-i), DP[j])

    if DP[-1] == 2000000:
        return -1
    else:
        return DP[-1]

print(solution(N, block))