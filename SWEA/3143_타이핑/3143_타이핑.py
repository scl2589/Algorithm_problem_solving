T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    N = len(A)
    M = len(B)
    i = 0
    cnt = 0
    while i<=N-M:
        j = 0
        while j<M and A[i+j] ==B[j]:
            j += 1
        if j == M:
            i += M
            cnt += 1
        else:
            i += 1
    print('#{} {}'.format(tc, N-M*cnt, cnt))