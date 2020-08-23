# for 문을 너무 많이 사용한다.
# 별로 좋지 않은 풀이 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    W = [0] * N
    B = [0] * N
    R = [0] * N
    for i in range(N-2): # w 영역의 경계 i
        s1 = 0
        for p in range(i+1):
            for q in range(M):
                if flag[p][q] != 'W':
                    s1 += 1
        for j in range(i+1, N-1): 
            s2 = 0
            for p in range(i+1, j+1):
                for q in range(M):
                    if flag[p][q]!='B':
                        s2 += 1
