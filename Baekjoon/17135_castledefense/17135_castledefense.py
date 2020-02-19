from itertools import combinations
from copy import deepcopy
n, m, d = map(int, input().split())
pos = [list(map(int, input().split())) for _ in range(n)]


#궁수 자리 배치
tmp = [i for i in range(m)]
archers = list(combinations(tmp, 3))
kill = []

#궁수 위치의 combination을 탐색한다.
for archer in archers:
    arr = deepcopy(pos)
    killed = 0
    while True:
        #각 궁수마다 거리를 따진다
        for each in archer:
            ti, tj = -1, -1
            minD = d + 1
            for i in range(n):
                for j in range(m):
                    if arr[i][j] >= 1 and abs(i-n) + abs(j-each) <= d:
                        #적의 최단거리 갱신하기
                        if minD > (abs(i-n) + abs(j-each)) :
                            minD = (abs(i-n) + abs(j-each))
                            ti, tj = i, j
                        elif minD==(abs(i-n) + abs(j-each)) and j < tj:
                            ti, tj = i, j
            #만약 새로 받은 index가 초기화했던 index가 아니라면 1을 추가해 공격한 것을 표시해준다.
            if ti!= -1 and tj!= -1:
                arr[ti][tj] += 1

        #몇 명이 죽었는지 탐색한다.
        saved = []
        for i in range(n):
            for j in range(m):
                if arr[i][j] >= 2:
                    killed += 1
                    arr[i][j] = 0

        #적을 1칸씩 내려준다.
        arr.insert(0, list([0]*m))
        arr = arr[:n]


        num_of_enemy = 0

        #적의 수가 0 이면 break한다.
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    num_of_enemy +=1
                    break
            if num_of_enemy >= 1:
                break

        if num_of_enemy == 0:
            kill.append(killed)
            break

print(max(kill))