# 다른 사람 코드

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]
re_dir = [0, 2, 1, 4, 3]

def move(ar):
    # 빈 딕셔너리를 만들어준다.
    temp = {}
    for ind, val in ar.items():
        x = ind[0]
        y = ind[1]
        num = val[0] ## 현재 미생물의 수
        dire = val[1] ## 방향
        cu_init_num = val[2] # 초기 미생물의 수
        nx = x + dx[dire-1]
        ny = y + dy[dire-1]

        if nx == 0 or nx == N-1 or ny == 0 or ny == N-1: #만약 끝에 닿았다면
            num = num // 2 # 수를 반절 줄이고
            dire = dire_reverse[dire-1] # 방향을 반대로 바꾼다.

        if not temp.get((nx, ny)):
            # 만약 해당 키에 해당하는 값이 없는 최초의 값이면
            # num, dire, num으로 초기값을 넣어준다.
            temp[(nx, ny)] = [num, dire, num]
        else:
            # 만약 이미 존재하는 값이 있으면, 그 값을 불러온다
            prev_num, prev_dire, init_num = temp.get((nx, ny))
            # 만약 이전에 존재하는 미생물의 초기값 init_num이 현재의 초기값 cu_init_num보다 클때
            if init_num > cu_init_num:
                # 방향을 prev_dire기준으로하고, 미생물을 더해준다.
                temp[(nx, ny)] = [num+prev_num, prev_dire, init_num]
            else:
                temp[(nx, ny)] = [num+prev_num, dire, cu_init_num]
    # 모든 과정이 끝나고, 언제 value 값이 3번째인 init_num을 현재의 미생물의 값이 value의 1번
    # 이렇게 하지 않을 시, 합쳐진 미생물의 초기값으로 안바꿔져서 45번째까지밖에 통과를 못한다.
    for i, val in temp.items():
        if val[0] != val[2]: # val[0]과 val[2]가 같지 않다는 것은 한번이라도 합쳐진 곳이기떄문이다.
            # val[2]의 초기값을 바꿔준다
            temp[ind] = [val[0], val[1], val[0]]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    
    arr = {}

    ### 딕셔너리로 각 (x, y)좌표를 기준으로 값을 넣어준다. 
    for _ in range(K):
        temp = list(map(int, input().split()))
        arr[(temp[0], temp[1])] = [temp[2], temp[3], temp[2]]
    
    for i in range(M):
        arr = move(arr)

    total = 0
    # arr의 value 값을 가져와서 그 중 미생물 수만 다해준다.
    for i in arr.values():
        total +i[0]
    print('#{} {}'.format(tc, total))