def clockwise(direction, disk):
    if direction == 0:
        save = disk[-1]
        for i in range(len(disk)-1, 0, -1):
            disk[i] = disk[i-1]
        disk[0] = save
    elif direction == 1:
        save = disk[0]
        for i in range(len(disk)-1):
            disk[i] = disk[i+1]
        disk[-1] = save


#n:원판의 개수, m: 1개의 원판당 적힌 숫자, T: 회전 횟수
n, m, t = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

#회전 횟수
for _ in range(t):
    # 각 회전 횟수마다 x, d, k 를 받는다.
    # x: x의 배수인 원판을 회전
    # d:0인 경우에는 시계 방향, 1인경우에는 반시계
    # k: 몇 칸 회전?
    x, d, k = map(int, input().split())

    #지워야 할 숫자(i, j) 표시하기 위한 배열
    check = [[False] * m for _ in range(n)]

    #회전을 실행한다.
    for i in range(len(arr)):
        if i % x == x-1:
            for _ in range(k):
                clockwise(d, arr[i])

    # 숫자가 바뀌었는지 확인하기 위한 변수
    changed = False

    #숫자끼리 비교하자
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                # arr[i][j]와 같은 값이 있는지 확인하기 위한 변수
                flag = False
                if j == 0:
                    if arr[i][0] == arr[i][-1]:
                        check[i][0] = True
                        check[i][-1] = True
                #4방향으로 확인해보기!
                for k in range(4):
                    # 만약 인접 숫자와 숫자가 같다면, 그 옆까지 같은지 확인하기 위해 만든 변수
                    marker = 1
                    while True:
                        current_i = i + di[k] * marker
                        current_j = j + dj[k] * marker
                        #current_i와 current_j가 0과 n, m을 넘어가는지 확인하자.
                        if 0<= current_i < n and 0 <= current_j < m:
                            #만약 숫자가 같다면 check에 마킹하고, 다음 숫자까지 같은지 확인하기 위해 marker +1해주자
                            if arr[i][j] == arr[current_i][current_j] :
                                check[current_i][current_j] = True
                                marker += 1
                                changed = True
                                flag = True
                            #만약 인접 숫자가 아니라면 break!
                            else:
                                break
                        else:
                            break
                #만약 arr[i][j]와 같은 값이 있다면, arr[i][j]가 0으로 변해야한다고 표시해주기
                if flag:
                    check[i][j] = True

    #만약 인접숫자가 같은 경우가 있다면, check와 대조해서 arr[i][j]를 0으로 바꿔주기
    if changed:
        for i in range(n):
            for j in range(m):
                if check[i][j]:
                    arr[i][j] = 0

    #인접 숫자가 없다면 평균구해서 +1, -1 해주기
    if not changed:
        total = 0
        dividend = 0
        for i in range(n):
            for j in range(m):
                total += arr[i][j]
                if arr[i][j] != 0:
                    dividend += 1
        if dividend != 0:
            average = total / dividend
            #평균보다 큰 수는 1을 빼고, 작은수에는 1을 더한다
            for i in range(n):
                for j in range(m):
                    if arr[i][j]!=0 and arr[i][j] > average:
                        arr[i][j] -= 1
                    elif arr[i][j]!= 0 and arr[i][j] < average:
                        arr[i][j] += 1

sum = 0
for i in range(n):
    for j in range(m):
        sum += arr[i][j]
print(sum)

