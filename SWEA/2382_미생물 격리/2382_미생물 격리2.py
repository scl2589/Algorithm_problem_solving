di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]
re_dir = [0, 2, 1, 4, 3]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    
    # K 개의 미생물 군집 정보
    # 세로 위치, 가로 위치, 미생물 수, 이동방향 순
    cells = [list(map(int, input().split())) for _ in range(K)]

    field = [[1]*N for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, N-1):
            field[i][j] = 0
    # M 시간동안
    for t in range(M):
       # 군집이 이동할 좌표의 정보를 기록할 dictionary 만들기
       space_info = {}
       # 각 군집 움직여보기 
       for cell in cells:
           direction = cell[3]
           ti, tj = cell[0], cell[1]
           cell_cnt = cell[2]
           ni = ti+ di[direction]
           nj = tj + dj[direciton]
           # 이동 위치에 약품이 있는 경우 (가장 자리를 1로 하고, 중심부는 0)
           if field[ni][nj] == 1:
               half_cell_cnt = cell_cnt //2
               space_info[(ni, nj)] = [half_cell_cnt, (cell_cnt, re_dir[direction])]
            else:
                # 이동 위치에 세포가 없으면
                if (ni, nj) not in space_info:
                    space_info[(ni, nj)] = [cell_cnt, (cell_cnt, direction)]
                else:
                    total_cell = space_info[(ni, nj)][0] + cell_cnt
                    # 현재 군집의 세포수가 더 많을 경우
                    if cell_cnt > space_info[(ni, nj)][1][0]:
                        space_info[(ni, nj)][0] = [total_cell,(cell_cnt, direction)]
                    else:
                        space_info[(ni, nj)][0] = total_cell
        # 세포들 상태 최신화
        new_cells = []
        for key, values in space_info.items():
            if values[0] != 0:
                new_cells.append([key[0], key[1], values[0], values[1]])
        cells = new_cells
    # 남아있는 세포 수 확인
    ans = 0
    for cell in cells:
        ans += cell[2]
    print('#{} {}'.format(tc, ans))
                    