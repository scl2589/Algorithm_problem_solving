T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = {0}
    for i in nums:
        for j in list(result):
            result.add(i+j)
    print('#{} {}'.format(tc, len(result)))