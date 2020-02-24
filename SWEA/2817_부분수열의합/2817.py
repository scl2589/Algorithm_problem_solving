def dfs(depth):
    global current
    global count
    if depth == N:
        if current == K:
            count += 1
        return
    dfs(depth+1)
    current += nums[depth]
    dfs(depth+1)
    current -= nums[depth]


T = int(input())

for tc in range(1, T+1):
    count = 0 
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    current = 0 
    dfs(0)

    print('#{} {}'.format(tc, count))
