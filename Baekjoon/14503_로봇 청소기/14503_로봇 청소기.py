'''
청소하는 영역의 개수 구하기

지도
- N x M 크기의 직사각형에 로봇 청소기 존재
- 지도의 각 칸은 (r, c)로 나타낼 수 있다.
- 각각의 칸은 벽 또는 빈 칸 
- 청소기가 바라보는 방향은 동/서/남/북

로봇청소기 작동방식
1. 현재 위치 청소
2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색 진행! 
- 왼쪽 방향 청소하지 않은 공간 o-> 그 방향으로 회전 후 한 칸 전진 후 1번(청소)부터 진행
- 왼쪽 방향 청소할 공간 x -> 그 방향으로 회전 후 2번으로 돌아감.
- 4개 방향 모두 청소 or 벽 -> 바라보는 방향 유지 및 한 칸 후진 후 2번 돌아감 
- 4개 방향 모두 (청소 or 벽) And 뒤쪽 방향 (후진하는 곳)도 벽이면 작동을 멈춘다. 

# d는 방향 0, 1, 2, 3 = 북, 동, 남, 서
# 빈칸은 0, 벽은 1 (벽은 통과할 수 없다.)
'''
dir = {
    # 북쪽 
    0: [0, -1],
    # 동쪽
    1: [-1, 0],
    # 남쪽
    2: [0, 1],
    # 서쪽
    3: [1, 0]
}
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

r -= 1
c -= 1

# 현재 위치를 청소한다.
arr[r][c] = -1
answer = 1

for j in arr:
    print(j)

while True:
    # 현재 방향 기준으로 왼족 방향부터 진행
    for _ in range(4): 
        ni = r + dir[d][0]
        nj = c + dir[d][1]
        # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면? 
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            print("뿅", ni, nj, d)
            # 청소한 칸으로 변경 
            arr[ni][nj] = -1
            answer += 1
            d  = (d-1) % 4
            r, c = ni, nj 
            break 
        # 왼쪽 방향에 청소할 공간이 없다면 그 방향으로 회전하기. 
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0:
            print("제자리 회전~~", ni, nj)
            d = (d-1) % 4
            
    # 네 방향 이미 청소되어 있거나 벽인 경우, 
    else:
        # 바라보는 방향 유지 후 
        ni = r + dir[d][1] 
        nj = c + dir[d][0]
        # 후진이 가능하다면 한 칸 후진 
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            arr[ni][nj] = -1
            answer += 1
        else:
            # 4개 방향 모두 (청소 or 벽) And 뒤쪽 방향 (후진하는 곳)도 벽이면 작동을 멈춘다. 
            print("으악", ni, nj)
            for i in arr:
                print(i)
            break 
print(answer)
