# MxM 크기의 숫자판이 있습니다. N개의 양의 정수로 구성된 수열이 주어질 때, 숫자판의 숫자를 따라 상하좌우로 이동해 주어진 수열을 찾을 수 있으면 1, 없으면 0을 출력하는 프로그램을 작성하세요. 
# 각 칸의 숫자는 1번만 사용할 수 있습니다.

# 예를 들어 1234563이란 수열을 아래의 숫자판에서는 완성할 수 없습니다.

# 0 0 0 0 0
# 0 1 2 0 0
# 0 6 3 0 0
# 0 5 4 0 0 
# 0 0 0 0 0

# 다음의 경우는 완성할 수 있습니다.
# 0 0 0 0 0
# 0 1 2 0 0
# 0 6 3 0 0
# 0 5 4 0 0 
# 0 0 3 2 1

# 입력
# 첫 줄에 테스트케이스 개수 T, 다음 줄부터 테스트케이스 별로 수열의 길이 N, 다음 줄에 N개의 수, 숫자판의 크기 M, 다음 줄 부터 M개의 줄에 걸쳐 M개씩의 숫자가 주어집니다. (5 <= N, M <=10)

# 출력
# #과 테스트케이스 번호, 빈칸에 이어 0 또는 1을 출력합니다.

def f(n, k, i, j):
    if n == k-1:
        return 1
    else:
        # v[i][j] = 1
        for a in range(4):
            ni = i + di[a]
            nj = j + dj[a]
            if 0<=ni < M and 0 <= nj <M and v[ni][nj] == 0:
                if num[n+1]==arr[ni][nj]:
                    v[ni][nj] = 1
                    if f(n+1, k, ni, nj) == 1:
                        return 1
                v[ni][nj] = 0
        return 0


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    M = int(input())
    arr = [list(map(int, input().split())) for _ in range(M)]
    v = [[0] * M for _ in range(M)]
    flag = True

    for i in range(M):
        for j in range(M):
            if arr[i][j] == num[0]:
                res = f(0, len(num), i, j)
                if res == 1:
                    print('#{} 1'.format(tc))
                    flag = False
                    break
        if not flag:
            break

    if flag:
        print('#{} {}'.format(tc, 0))
