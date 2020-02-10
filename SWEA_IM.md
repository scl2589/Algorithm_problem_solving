# SWEA IM Algorithm Questions

#### 2001. 파리 퇴치

```python
trial = int(input())

for i in range(trial):
    n, m = map(int, input().split(' '))
    list1 = []
    for _ in range(n):
        numbers = list(map(int,input().split(' ')))
        list1.append(numbers)
    max = 0
    for j in range(0, n-m+1):      
        for k in range(0, n-m+1):          
            sum = 0
            for l in range(0, m): #가로
                for u in range (0, m): #세로
                #sum += list1[j][l-1]+list1[j][l]
                	sum += list1[j+u][k+l]
            if sum >= max:
                max = sum
    print(f'#{i+1} {max}')
```



#### 1206. View

강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.

이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.

그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.

빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.

아래와 같이 강변에 8채의 빌딩이 있을 때, 연두색으로 색칠된 여섯 세대에서는 좌우로 2칸 이상의 공백이 존재하므로 조망권이 확보된다. 따라서 답은 6이 된다.

```python
for tc in range(1, 11):
    n = int(input())
    buildings=list(map(int,input().strip().split(' ')))
    buildings= buildings+[0,0]
    total = 0
    for idx, value in enumerate(buildings):
        if 2<= idx <= len(buildings)-3:
            building_cluster = [buildings[idx-2],buildings[idx-1], buildings[idx+1], buildings[idx+2]]
            if value > max(building_cluster):
                total += value - max(building_cluster)
        
    print('#{} {}'.format(tc, total))


```



#### 1208. Flatten

한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.

주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다).

```python
for tc in range(1, 11):
    # 덤프 횟수 받기
    dumps = int(input())

    # 상자 높이 받기
    heights = list(map(int, input().split()))

    # 덤프 횟수 만큼 덤프 실행하기
    for i in range(dumps):
        highest = max(heights)
        lowest = min(heights)
        highindex = heights.index(highest)
        lowindex = heights.index(lowest)
        heights[highindex] -= 1
        heights[lowindex] += 1

    result = max(heights) - min(heights)

    # 최고점, 최저점 반환하기
    print('#{} {}'.format(tc, result))
```

```python
for tc in range(1, 11):
    # 덤프 횟수 받기
    dumps = int(input())

    # 상자 높이 받기
    heights = list(map(int, input().split()))

    # 덤프 횟수 만큼 덤프 실행하기
    for i in range(dumps):
        highest = max(heights)
        lowest = min(heights)
        highindex = heights.index(highest)
        lowindex = heights.index(lowest)
        heights[highindex] -= 1
        heights[lowindex] += 1

    result = max(heights) - min(heights)

    # 최고점, 최저점 반환하기
    print('#{} {}'.format(tc, result))
```



#### 4826. Min Max

N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

```python
trial = int(input())
for tc in range(1, trial + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    for idx, num in enumerate(nums):
        if idx == 0:
            max = num
            min = num
        else:
            if num > max:
                max = num
            elif num < min:
                min = num
    difference = max- min
    print('#{} {}'.format(tc, difference))

```





#### 4834. 숫자 카드

0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

```python
from collections import Counter

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    d = list(input())
    c = [0] * 10

    for i in range(n):
        c[int(d[i])] += 1

    max_idx = 0
    max_value = c[0]

    for i in range(1,10):
        if max_value <= c[i]:
            max_value = c[i]
            max_idx = i

    print('#{} {} {}'.format(tc, max_idx, max_value))
```





#### 4835. 구간합

N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.


```python
from collections import Counter
import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    d = list(input())
    c = [0] * 10

    for i in range(n):
        c[int(d[i])] += 1

    max_idx = 0
    max_value = c[0]

    for i in range(1,10):
        if max_value <= c[i]:
            max_value = c[i]
            max_idx = i

    print('#{} {} {}'.format(tc, max_idx, max_value))
```





#### 5431. 민석이의 과제 체크하기

```python
trial = int(input())
for tc in range(1, trial+1):
    N, K = map(int, input().split())
    submitted = list(map(int, input().split()))

    #학생 번호를 정렬하는 arr를 만들자
    students = [i for i in range(1, N+1)]

    #제출한 학생을 array에서 삭제하자
    for i in submitted:
        if i in students:
            students.remove(i)

    print('#{} {}'.format(tc, ' '.join(map(str, students))))
```





#### 1970. 쉬운 거스름돈

```python
trial = int(input())
for i in range(trial):
    get = int(input())
    money = get - get%10
    print(f'#{i+1}')
    a = money // 50000
    money -= 50000 * a  
    b = money // 10000
    money -= 10000 * b
    c = money // 5000
    money -= 5000 * c
    d = money // 1000
    money -= 1000 * d
    e = money // 500
    money -= 500 * e
    f = money // 100
    money -= 100 * f
    g = money //50
    money -= 50 * g
    h = money //10
    money -= 10 * h
    print(a, b, c, d, e, f, g, h)
```

```python
for i in range(int(input())):
    m=int(input())
    l=[50000,10000,5000,1000,500,100,50,10]
    print(f'#{i+1}')
    for j in range(8):
        print(m//l[j],end=' ')
        m=m%l[j]
    print( )
```



#### 1959. 두 개의 숫자열

```python
trial = int(input())
for tc in range(trial):
    n, m = map(int, input().split(' '))
    alist= list(map(int,input().split(' ')))
    blist= list(map(int,input().split(' ')))

    if n > m:
        difference = n - m
        max = 0
        for b in range(difference+1):
            sum = 0
            for a in range(m):
                sum += blist[a]*alist[a+b]
            if sum >= max:
                max = sum

    else:
        difference = m- n
        max = 0
        for b in range(difference+1):
            sum = 0
            for a in range(n):
                sum += alist[a]*blist[a+b]
            if sum >= max:
                max = sum
    print(f'#{tc+1} {max}')


```

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(A)>len(B):
        arr1 = A
        arr2 = B
    else:
        arr1 = B
        arr2 = A

    total = []
    for i in range(len(arr1)-len(arr2)+1):
        temp = 0
        for j in range(len(arr2)):
            temp += arr2[j] * arr1[i+j]
        total.append(temp)

    print('#{} {}'.format(tc,max(total)))

```



#### 1209. Sum

```python
for tc in range(1, 11):
    num = int(input())
    tenthousand = []
    for i in range(100):
        hundred = list(map(int, input().strip().split()))
        tenthousand.append(hundred)
    temp = []
    for i in range(100): #가로 살펴보기
        total = sum(tenthousand[i][0:100])
        temp.append(total)

    maximum = 0
    for row in range(100): #세로 살펴보기
        total = 0
        for column in range(100):
            total += tenthousand[column][row]
        if total > maximum:
            maximum = total
    temp.append(maximum)

    total = 0
    total2 = 0
    for k in range(100): #대각선 살펴보기
        total += tenthousand[k][k]
        total2 += tenthousand[k][99-k]
    temp.append(total)
    temp.append(total2)

    print('#{} {}'.format(tc, max(temp)))


```





#### 4836. 색칠하기

그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.

예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.

2

2 2 4 4 1 ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )

3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )

```python
trial = int(input())
for tc in range(1, trial + 1):
    n = int(input())
    cubes = []
    arr = []
    for i in range(10):
        arr.append([0]*10)
    for _ in range(n):
        cubes.append(list(map(int, input().split())))

    for cube in cubes:
        r1, c1, r2, c2, color = cube[0], cube[1], cube[2], cube[3], cube[4]
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[i][j] += color
    count = 0
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x][y] >= 3:
                count += 1


    print('#{} {}'.format(tc, count))

```

```python
# 1. 10 * 10 격자를 생성
# 2. input으로 주어진 조건에 따라 색칠
#   - 왼쪽 상단 인덱스 & 오른쪽 하단 인덱스
# 3. 겹쳐진 구간의 개수 출력

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    tile = [[0] * 10 for _ in range(10)]
    
    for _ in range(N):
        r1, c1, r2, c2, color = map(int,input().split())

        #x축의 범위
        for i in range(r1, r2+1):
            #y축의 범위
            for j in range(c1, c2+1):
                tile[i][j] += color
                if tile[i][j] == 3:
                    cnt +=1
    
    print('#{} {}'.format(tc, cnt))
    

```





#### 4843. 특별한 정렬

보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
 

10 1 9 2 8 3 7 4 6 5

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

```python
trial = int(input())
for tc in range(1, trial + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    s = sorted(numbers)
    correct = s[:6]
    reverse = s[::-1]
    reverse = reverse[:6]

    result = []
    for i in range(5):
        result.append(reverse[i])
        result.append(correct[i])

    result = map(str, result)
    result = ' '.join(result)

    print('#{} {}'.format(tc, result))
```

```python
trial = int(input())
for tc in range(1, trial + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    s = sorted(numbers)
    correct = s[:6]
    reverse = s[::-1]
    reverse = reverse[:6]

    result = []
    for i in range(5):
        result.append(reverse[i])
        result.append(correct[i])

    result = map(str, result)
    result = ' '.join(result)

    print('#{} {}'.format(tc, result))
```





#### 1210. Ladder1

점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.

김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.

사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자.

아래 <그림 1>의 예를 살펴보면, 출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 추가되고(이 예에서는 2개가 추가됨) 이 막대들 사이에 가로 방향의 선들이 또한 랜덤하게 연결된다.

X=0인 출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.

방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.

문제의 X표시에 도착하려면 X=4인 출발점에서 출발해야 하므로 답은 4가 된다. 해당 경로는 별도로 표시하였다.

아래 <그림 2>와 같은 **100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서, 모든 출발점을 검사하여 가장 짧은 이동 거리를 갖는 시작점 x(복수 개인 경우 가장 큰 x좌표)를 반환하는 코드를 작성하라.**(‘0’으로 채워진 평면상에 사다리는 연속된 ‘1’로 표현된다. 도착 지점은 '2'로 표현된다.)

```python
T = 10
for tc in range(1, T + 1):
    trial = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))

    # 맨 윗줄에 1인 숫자 세기
    start = []
    for i in range(100):
        if arr[0][i] == 1:
            start.append(i)

    # j는 열의 시작점을 말한다.
    result = []
    counters = []
    for j in start:
        count = 0
        total = 0
        move = 0
        i = 1
        while i < 100:
            if i < 99:
                if j + move == 99:
                    if arr[i][j - 1 + move] == 1:
                        while arr[i][j - 1 + move] == 1:
                            count += 1
                            move -= 1
                        i += 1
                        count += 1
                    else:
                        count += 1
                        i += 1

                elif j + move == 0:
                    if arr[i][j + 1 + move] == 1:
                        while arr[i][j + 1 + move] == 1:
                            count += 1
                            move += 1
                        i += 1
                        count += 1
                    else:
                        count += 1
                        i += 1
                else:
                    if arr[i][j - 1 + move] == 1:
                        while arr[i][j - 1 + move] == 1:
                            count += 1
                            move -= 1
                            if j - 1 + move < 0: ####
                                break
                        i += 1
                        count += 1

                    elif arr[i][j + 1 + move] == 1:
                        while arr[i][j + 1 + move] == 1:
                            count += 1
                            move += 1
                            if j + 1 + move > 99:
                                break
                        i += 1
                        count += 1

                    else:
                        count += 1
                        i += 1
            elif i == 99:
                i += 1
        counters.append(count)
        result.append(j + move)

    startings = []

    for idx, value in enumerate(counters):
        if value == min(counters):
            startings.append(start[idx])


    print('#{} {}'.format(tc, max(startings)))

```

```python
T = 10
for _ in range(T):
    tx = int(input())
    d = [list(map(int, input().split())) for _ in range(100)]
 
    result = 1000
    cnt = 1000000
    # 각 사다리 점검하기.
    for i in range(99, -1, -1):
        c = i
        r = 0
        temp = 0
 
        if d[r][c]:
            while r != 99:
                if c != 99 and d[r][c+1]:
                    while c < 99 and d[r][c+1]:
                        temp += 1
                        c += 1
                elif c != 0 and d[r][c-1]:
                    while c > 0 and d[r][c-1]:
                        temp += 1
                        c -= 1
                r = r+1
                temp += 1
            if cnt > temp:
                cnt = temp
                result = i
    print('#{} {}'.format(tx, result))
```



#### 1211. Ladder2

```python

```





#### 1220. Magnetic

```python

```





#### 1258. 행렬찾기

```python

```





#### 1974. 스도쿠검증

```python
trial = int(input())
for i in range(trial):
    sudoku = []
    count = 0
    breakcount = 0

    for _ in range(9):  # 수도쿠 만들기
        sudoku.append(list(map(int, input().strip().split(' '))))

    for j in range(len(sudoku)):  # 가로 확인하기
        temp = sorted(sudoku[j])
        if temp != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print(f'#{i+1} 0')
            breakcount += 1
            break
        else:
            count += 1


    for row in range(9):  # 세로 확인하기
        temp = []
        for column in range(9):
            temp.append(sudoku[column][row])
        if sorted(temp) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if breakcount >= 1:
                break
            else:
                breakcount += 1
                print(f'#{i+1} 0')
                break
        else:
            count += 1

    for a in range(0, 9, 3):  # 네모칸 확인하기
        for b in range(0, 9, 3):
            temp = []
            for c in range(3):
                temp.append(sudoku[a][b + c])
                temp.append(sudoku[a + 1][b + c])
                temp.append(sudoku[a + 2][b + c])
            if sorted(temp) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if breakcount >= 1:
                    break
                else:
                    breakcount += 1
                    print(f'#{i+1} 0')
                    break
            else:
                count += 1

    if count == 27:
        print(f'#{i+1} 1')



```





#### 1961. 숫자 배열 회전

```python
trial = int(input())
for i in range(trial):
    n = int(input())
    list1 = []
    newlist1 = []
    newlist2=[]
    newlist3=[]
    for j in range(n):
        list1.append(list(map(int, input().strip().split(' '))))
    for a in range(0, n):  # 90
        list2= []
        for b in range(n - 1, -1, -1):
            list2.append(list1[b][a])
        newlist1.append(list2)

    for c in range(0, n):  # 90
        list2 = []
        for d in range(n - 1, -1, -1):
            list2.append(newlist1[d][c])
        newlist2.append(list2)

    for e in range(0, n):  # 90
        list2 = []
        for f in range(n - 1, -1, -1):
            list2.append(newlist2[f][e])
        newlist3.append(list2)
    print(f'#{i+1}')
    for g in range(n): # 출력하기
        print(*newlist1[g]," ",*newlist2[g]," ",*newlist3[g], sep='')


```





#### 4466. 최대 성적표 만들기

```python
trial = int(input())
for tc in range(1, trial+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    ascending= sorted(scores)
    total = sum(ascending [-1:-1-K:-1] )

    print('#{} {}'.format(tc, total))
```





#### 1979. 어디에 단어가 들어갈 수 있을까

```python
trial = int(input())
for i in range(trial):
    n, k = map(int, input().split(' '))
    puzzle = []


    for j in range(n):
        line = list(map(int,input().split()))
        puzzle.append(line)

    row_count, col_count = 0, 0

    for vertical in range(n):  # 가로 살펴보기
        count = 0
        for horizontal in range(n):
            if puzzle[vertical][horizontal]==1:
                count += 1
            if horizontal == n-1 or puzzle[vertical][horizontal]==0:
                if count==k:
                    row_count +=1
                count = 0


    for horizontal in range(n):  # 세로 살펴보기
        count = 0
        for vertical in range(n):
            if puzzle[vertical][horizontal]==1:
                count += 1
            if vertical == n-1 or puzzle[vertical][horizontal]==0:
                if count == k:
                    col_count += 1
                count = 0

    print(f'#{i + 1} {row_count + col_count}')


```

```python
T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    #가로 확인하기
    scores = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
                #1의 개수가 단어 길이와 같다면 점수 주기
                if count == K:
                    scores += 1
                #만약 1의 개수가 단어길이보다 높다면 점수 빼기
                elif count > K:
                    scores -= 1
                    count = 0
            elif arr[i][j]== 0:
                #0을 만난다면 카운트는 0!
                count = 0


    #세로 확인하기
    for j in range(N):
        count = 0
        for i in range(N):
            if arr[i][j] == 1:
                count += 1
                #1의 개수가 단어 길이와 같다면 점수 주기
                if count == K:
                    scores += 1
                #만약 1의 개수가 단어길이보다 높다면 점수 빼기
                elif count > K:
                    scores -= 1
                    count = 0
            elif arr[i][j]== 0:
                #0을 만난다면 카운트는 0!
                count = 0

    print('#{} {}'.format(tc, scores))

```





#### 2805. 농작물 수확하기

```python
trial = int(input())
for tc in range(1, trial + 1):
    N = int(input())
    field = []
    for i in range(N):
        temp = list(map(int,list(input())))
        field.append(temp)

    standard = N // 2
    total = 0
    #위 파트
    for j in range(standard):
        total += sum(field[j][standard - j : standard + j + 1])
            #print(total)
    
    #가운데
    total += sum(field[standard])
    
    #아래 파트
    for i in range(N-1, standard, -1):
        diff = N-1-i
        total += sum(field[i][standard-diff : standard+diff+1])
    
    print('#{} {}'.format(tc, total))
        

```





#### 6190. 정곤이의 단조 증가하는 수

```python
trial = int(input())
for tc in range(1, trial+1):
    N = int(input())
    nums = list(map(int, input().split()))

    result = []
    final = []


    for i in range(N):
        for j in range(i+1, N):
            result.append(str(nums[i]*nums[j]))


    for num in result:
        count = 0
        for each in range(len(num)-1):
            if len(num) >= 2:
                if num[each] <= num[each+1]:
                    count += 1
        if count == len(num)-1:
            final.append(int(num))


    if final == []:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, max(final)))

```





#### 1221. GNS

```python
trial = int(input())
for tc in range(1, trial+1):
    T, length = map(str, input().split())
    numbers = list(map(str, input().split()))
    dictionary = {
        "ZRO" : 0,
        "ONE" : 0,
        "TWO" : 0,
        "THR" : 0,
        "FOR" : 0,
        "FIV" : 0,
        "SIX" : 0,
        "SVN" : 0,
        "EGT" : 0,
        "NIN" : 0,
    }

    for i in numbers:
        dictionary[i] += 1

    onlykeys = list(dictionary.keys())

    print('#{}'.format(tc))
    for j in range(len(dictionary)):
         print((onlykeys[j]+' ') * dictionary[onlykeys[j]], end = ' ')


```





#### 1215. 회문1

```python
for tc in range(1, 11):
    length = int(input())
    puzzles = []
    for i in range(8):
        puzzle = list(input())
        puzzles.append(puzzle)

    count = 0
    for horizontal in range(0, len(puzzles)):  # 가로 살펴보기
        for each in range(0,len(puzzles)-length+1):
            word = puzzles[horizontal][each:each+length]
            if word == word[::-1]:
                count += 1

    for vertical in range(0, len(puzzles)):  # 세로 살펴보기
        for each in range(0, len(puzzles) - length + 1):
            word = ''
            for num in range(0, length):
                word += puzzles[each + num][vertical]
            if word == word[::-1]:
                count += 1

    print('#{} {}'.format(tc, count))
```





#### 1216. 회문2

```python

```



#### 1267. 작업순서

```python

```



