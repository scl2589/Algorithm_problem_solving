# 선생님 풀이
# A형의 절반 과정

for tc in range(1, int(input())):
    N, M = map(int, input())
    flag = [list(input()) for _ in range(N)]
    W, B, R = [0] * N
    for i in range(N):
        for j in range(M):
            if flag[i][j]!= 'W':
                W[i] += 1
            if flag[i][j]!= 'B':
                B[i] += 1
            if flag[i][j]!= 'R':
                R[i] += 1
    for i in range(1, N):
        W[i] += W[i-1]
        B[i] += B[i-1]
        R[i] += R[i-1]
    
    minV = N * M
     
    for i in range(N-2):
        for j in range(i+1, N-1):
            s1 = W[i]
            s2 = B[j] - B[i]
            s3 = R[N-1] - R[j]
            if minV > s1+s2+s3: 
                minV = s1+s2+s3
    print(f"#{tc} {minV}")


