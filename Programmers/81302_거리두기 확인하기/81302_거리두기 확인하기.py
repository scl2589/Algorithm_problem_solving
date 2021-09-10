def check_surround(i, j, places):
    # 어느쪽 방향을 확인해야하는지 체크 
    # X 가 파티션, O는 빈 테이블 
    # i가 왼쪽, j가 오른쪽인 경우
    temp2=[]
    if i[0] == j[0]:
        temp = places[i[0]][i[1]+1]
    # i가 위쪽, j가 아래쪽인 경우 
    elif i[1] == j[1]:
        temp = places[i[0]+1][i[1]]
    # j가 i의 왼쪽 대각선에 있는 경우
    elif i[0] < j[0] and i[1] > j[1]:
        temp = places[i[0]][i[1]-1]
        temp2 = places[i[0]+1][i[1]]
    # j가 i의 오른쪽 대각선에 있는 경우
    elif i[0] < j[0] and i[1] < j[1]:
        temp = places[i[0]][i[1]+1]
        temp2 = places[i[0]+1][i[1]]
    if temp == 'O':
        return False
    elif temp == 'X':
        if len(temp2) != 0 and temp2 == 'O':
            return False
        return True


def check_dist(i, j, places):
    dist = abs(i[0]-j[0]) + abs(i[1]-j[1])
    if dist >= 3:
        return True
    elif dist == 1:
        return False
    elif dist == 2:
        if check_surround(i, j, places):
            return True
        else:
            return False

def check_rule(pos, places):
    for idx1 in range(len(pos)-1):
        i = pos[idx1]
        for idx2 in range(idx1+1, len(pos)):
            j = pos[idx2]
            if not check_dist(i, j, places):
                return False
    return True 
            

def solution(places):
    answer = []
    
    for i in range(len(places)):
        pos = []
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == 'P':
                    pos.append([j, k])
        # P (응시자)가 없는 경우
        if not pos:
            answer.append(1)
        # 응시자가 있다면 
        else:
            # 거리 확인하기
            if check_rule(pos, places[i]):
                answer.append(1)
            else:
                answer.append(0)
            
    return answer