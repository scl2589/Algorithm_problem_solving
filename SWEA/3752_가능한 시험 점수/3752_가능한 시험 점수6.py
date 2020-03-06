#제한시간 초과 코드 (재귀)
'''
시간이 초과되는 이유는: 
우선, not in은 O(n) 연산자이기 때문에 set자료형에 넣어서 시간을 줄여야 하는데
set자료형에 넣어도 시간초과가 나는 상태이다.
그렇기 때문에 이 코드 말고 check배열을 만들어서 걸러줘야 한다.
'''
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
