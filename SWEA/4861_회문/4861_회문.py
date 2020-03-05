import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    answer = ''


    #가로 회문
    for i in range(N):
        for j in range(N-M+1):
            string = arr[i][j:j+M]
            if string == string[::-1]:
                answer = string

    #세로 회문
    for j in range(N):
        for i in range(N-M+1):
            string = ''
            for k in range(M):
                string+=arr[i+k][j]
            if string == string[::-1]:
                answer = string

    print('#{} {}'.format(tc, ''.join(answer)))
                

