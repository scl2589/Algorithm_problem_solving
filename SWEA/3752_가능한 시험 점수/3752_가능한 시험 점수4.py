#제한시간 초과 코드 (재귀)
def f(n, k, s):
    if n == k:
        if s not in result:
            result.add(s)
        return
    else:
        f(n+1, k, s+nums[n])
        f(n+1, k, s)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = set()
    check = [False] * N
    f(0, N, 0)
    print('#{} {}'.format(tc, len(result)))
