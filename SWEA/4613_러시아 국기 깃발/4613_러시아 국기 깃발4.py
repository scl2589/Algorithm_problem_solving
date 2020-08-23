for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    W = [0] * N
    R = [0] * N
    B = [0] * N
    flag = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if flag[i][j]!='W':
                W[i] += 1
            if flag[i][j]!='R':
                R[i] += 1
            if flag[i][j]!='B':
                B[i] += 1
    for i in range(1, N):
        R[i] += R[i-1]
        W[i] += W[i-1]
        B[i] += B[i-1]
    
    minV = float('inf')

    for i in range(N-2):
        for j in range(i, N-1):
            s1 = W[i]
            s2 = B[j] - B[i]
            s3 = R[N-1] - R[j]
            if minV > s1 + s2 + s3 :
                minV = s1 + s2 + s3
    print(f'#{tc} {minV}')
