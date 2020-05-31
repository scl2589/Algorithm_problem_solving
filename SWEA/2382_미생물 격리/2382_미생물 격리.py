# def dir(i, j, direction):
#     ni = i + di[direction]
#     nj = j + dj[direction]
    

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]
reverse_list =[0, 2, 1, 4, 3]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    
    # K 개의 미생물 군집 정보
    # 세로 위치, 가로 위치, 미생물 수, 이동방향 순
    info = [list(map(int, input().split())) for _ in range(K)]

    org = [[0]*N for _ in range(N)]

    mov = [[-1]*N for _ in range(N)]
    # 이동방향(상:1, 하:2, 좌: 3, 우: 4)

    for i in info:
        # 만약 방향이 있으면 
        if i[3] > 0:
            #dir(i[0], info[1], i[3])
            ni = i[0] + di[i[3]]
            nj = i[1] + dj[i[3]]
            # 가장 자리인 경우
            if ni == 0 or ni== N-1 or nj == 0 or nj == N-1:
                i[2] = i[2] //2
                if i[2]:
                    i[3] = reverse_list[i[3]]
                else:
                    i[3] = 0
            # 가장 자리가 아닌 경우
            else:
                if arr[ni][nj] == 0:
                    mov[ni][nj] = 
                    
