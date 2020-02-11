# 백준 IM 문제

#### 2669. 직사각형 네개의 합집합의 면적 구하기

```python
arr = [list(map(int, input().split())) for _ in range(4)]
x_maximum = 0
y_maximum = 0
for i in range(4):
    for j in range(0, 4, 2):
        if arr[i][j] > x_maximum:
            x_maximum = arr[i][j]
        if arr[i][j+1] > y_maximum:
            y_maximum = arr[i][j+1]


squares = [[0]*x_maximum for _ in range(y_maximum)]

for k in range(4):
    x1 = arr[k][0]
    y1 = arr[k][1]
    x2 = arr[k][2]
    y2 = arr[k][3]
    for i in range(y1+1, y2+1):
        for j in range(x1+1, x2+1):
            squares[i-1][j-1] += 1
count = 0
for i in range(y_maximum):
    for j in range(x_maximum):
        if squares[i][j] >=1:
            count +=1

print(count)


```



#### 2635. 수 이어가기

```python
N = int(input())

answer=[]
count =[]
for i in range(N):
    temp = [N, N-i]
    prev_N = N
    new_N = N-i
    insert_N = 100
    while insert_N >= 0:
        insert_N = prev_N - new_N
        if insert_N >= 0:
            temp.append(insert_N)
            prev_N = new_N
            new_N = insert_N
        else:
            break

    count.append(len(temp))
    answer.append(temp)

max_count = max(count)
index = count.index(max_count)

print(max_count)
print(*answer[index])
```

```python
#영찬오빠 버전
def carry(arr):
    if arr[-2]-arr[-1]<0:
        return arr
    arr.append(arr[-2]-arr[-1])
    return carry(arr)
s_num=int(input())
max_len=0
for i in range(1,s_num+1):
    arr =carry([s_num,i])
    if max_len<len(arr):
        max_len=len(arr)
        answers=arr
print(max_len)
print(*answers)
```



#### 1244. 스위치 켜고 끄기

```python
numofswi = int(input())
switches = list(map(int, input().split()))
numofstu = int(input())
order = []
for i in range(numofstu):
    x, y = map(int, input().split())
    order.append((x, y))

for i in order:
    # 남학생
    if i[0] == 1:
        # 남학생의 스위치 번호를 뽑아낸다
        idx = i[1]
        # 배수일 때 스위치를 바꾼다.
        for j in range(idx - 1, len(switches), idx):
            if switches[j] == 0:
                switches[j] = 1
            else:
                switches[j] = 0
    # 여학생
    else:
        # 여학생의 스위치 번호를 뽑아낸다
        idx = i[1]
        shorten = idx - 1

        # 양쪽의 스위치를 찾아본다.
        for j in range(1, len(switches)):
            if idx - j > 0 and idx + j <= len(switches):
                if switches[shorten - j] == switches[shorten + j]:
                    if switches[shorten - j] == 0:
                        switches[shorten - j] = 1
                        switches[shorten + j] = 1

                    else:
                        switches[shorten - j] = 0
                        switches[shorten + j] = 0

                else:
                    break
            else:
                break

        if switches[shorten] == 0:
            switches[shorten] = 1
        else:
            switches[shorten] = 0

for i in range(1, len(switches) + 1):
    if i % 20 == 0:
        print(switches[i - 1])
    else:
        print(switches[i - 1], end=' ')

```



#### 2628. 종이자르기

```python
x, y = map(int, input().split())
num_cut = int(input())
arr_for_count = [[1] * y for _ in range(x)]

# 가로 세로 commands
arr = [list(map(int, input().split())) for _ in range(num_cut)]

# 가로로 자르는 점선은 0으로 시작
# 세로로 자르는 점선은 1으로 시작

x_cut = [0]
y_cut = [0]
for i in arr:
    if i[0] == 0:
        y_cut.append(i[1])

    elif i[0] == 1:
        x_cut.append(i[1])
x_cut.append(x)
y_cut.append(y)
x_cut.sort()
y_cut.sort()

area = []
for i in range(len(y_cut)-1):
    for j in range(len(x_cut)-1):
        area.append((y_cut[i+1]-y_cut[i]) *(x_cut[j+1]-x_cut[j]))

print(max(area))


```



#### 2116. 주사위 쌓기

```python
num = int(input())
dices = []
for _ in range(num):
    dices.append(list(map(int, input().split())))

facing = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
maximum = 0


total = []
# 6개 각각의 베이스
for i in range(6):
    result = []
    ref = [1, 2, 3, 4, 5, 6]
    ref.remove(dices[0][i])
    next = dices[0][facing[i]]
    ref.remove(dices[0][facing[i]])
    result.append(max(ref))

    for j in range(1, len(dices)):
        ref = [1, 2, 3, 4, 5, 6]
        ref.remove(next)
        next = dices[j][facing[dices[j].index(next)]]
        ref.remove(next)
        result.append(max(ref))
    result = sum(result)
    if maximum < result:
        maximum = result

print(maximum)

```



#### 2304. 창고 다각형

```python
N = int(input())
columns = []
for _ in range(N):
    temp= tuple(map(int, input().split()))
    columns.append(temp)

columns.sort(key= lambda x:x[0])

area = 0
for i in range(len(columns)-1):

    heights = []
    for j in range(i, len(columns)):
        heights.append(columns[j][1])
        if columns[j][1] > columns[i][1]:
            this = columns[j][1]

    if columns[i+1][1] > columns[i][1]:
        x = columns[i + 1][0] - columns[i][0]
        area += x * columns[i][1]




```

```python
N = int(input())
columns = []
for _ in range(N):
    temp= tuple(map(int, input().split()))
    columns.append(temp)

columns.sort(key= lambda x:x[0])

increasing = [columns[0]]
maximum = 0


for i in range(1, len(columns)):
    if columns[i][1] > maximum:
        increasing.append(columns[i])
        maximum = columns[i][1]
    elif i == len(columns)-1:
        increasing.append(columns[i])
print(increasing)

area = 0
for i in range(len(increasing)-1):
    for j in range(i+1, len(increasing)):
        #heights.append(columns[j][1])
        # if columns[j][1] > columns[i][1]:
        #     this = columns[j][1]
        if increasing[j][1] > increasing[i][1]:
            x = increasing[j][0] - increasing[i][0]
            area += x * increasing[i][1]
            break
        elif increasing[j][1] < increasing[i][1]: ### 확인 필요...
            area += 1 * increasing[i][1]
            if j == len(increasing)-1:
                area += increasing[j][1] * (increasing[j][0]- increasing[i][0])
                break

print(area)



```



#### 2559. 수열

```python
N, K = map(int, input().split())
arr = list(map(int, input().split()))

arr2 = arr[0 : K]
total = sum(arr2)


if N == K:
    print(total)
else:
    maximum = total
    for i in range(K, N):
        arr2.append(arr[i])
        total += arr[i]
        total -= arr2[0]
        del arr2[0]
        if total > maximum:
            maximum = total

    print(maximum)

```



#### 2578. 빙고

```python
bingo = [list(map(int, input().split())) for _ in range(5)]
numbers = [list(map(int, input().split())) for _ in range(5)]

def find_bingo(bingo):
    total_bingo = 0
    shout_out_bingo = False
    #가로 체크하기
    for a in range(5):
        count_0 = 0
        for b in range(5):
            if bingo[a][b] == 0:
                count_0 += 1
        if count_0 == 5:
            total_bingo += 1

    #세로 체크하기
    for b in range(5):
        count_0 = 0
        for a in range(5):
            if bingo[a][b] == 0:
                count_0 += 1
        if count_0 == 5:
            total_bingo += 1

    #대각선 체크하기 (왼 --> 오)
    count_0 = 0
    for a in range(5):
        if bingo[a][a] == 0:
            count_0 += 1
    if count_0 == 5:
        total_bingo += 1

    #대각선 체크하기 (오 --> 왼)
    count_0 = 0
    for a in range(4,-1, -1):
        if bingo[4-a][a] == 0:
            count_0 += 1
    if count_0 == 5:
        total_bingo += 1



    #빙고인지 확인하기
    if total_bingo >= 3:
        shout_out_bingo = True

    return shout_out_bingo



count = 0
for i in range(5):
    for j in range(5):
        count += 1
        call = numbers[i][j]
        for k in range(5):
            for l in range(5):
                if bingo[k][l] == call:
                    bingo[k][l] = 0
                    break
        result = find_bingo(bingo)
        if result:
            print(count)
            break
    if result:
        break


```



#### 2477. 참외밭

```python

```



#### 2527. 직사각형

```python

```



#### 10157. 자리배정

```python

```



#### 10158. 개미

```python

```



#### 10163. 색종이

```python
T = int(input())
arr = [[0]*101 for _ in range(101)]

for i in range(1, T+1):
    r1, c1, r2, c2 = map(int, input().split())
    for k in range(r1, r2+1):
        for l in range(c1, c2+1):
            arr[k][l] = i

for i in range(1, T+1):
    count = 0
    for k in range(101):
        for l in range(101):
            if arr[k][l] == i:
                count += 1
    print(count)

```



#### 13300. 방 배정

```python
import math

#N = 학생 수를 말하며 k는 방의 최대인원수를 말한다
N, K = map(int, input().split())
students = []
for i in range(N):
    students.append(tuple(map(int, input().split())))

dictionary = {}
for i in students:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

counts = dictionary.values()
room = 0
for i in counts:
    room += math.ceil(i/ K)

print(room)



```



#### 14696. 딱지놀이

```python
T = int(input())
#A,B의 카드를 받자
A= []
B = []
for _ in range(T):
    A.append(list(map(int, input().split())))
    B.append(list(map(int, input().split())))

for i in range(T):
    cards_A= A[i][1:]
    cards_B= B[i][1:]
    for j in range(4, 0, -1):
        if cards_A.count(j) > cards_B.count(j):
            print('A')
            break
        elif cards_A.count(j) < cards_B.count(j):
            print('B')
            break
        if j == 1:
            print('D')

```



#### 2309. 일곱 난쟁이

```python
import itertools
heights = [int(input()) for i in range(9)]
cmb = []
cmb += itertools.combinations(heights, 7)

for i in cmb:
    if sum(i) == 100:
        valid_combos = sorted(list(i))

for i in valid_combos:
    print(i)
```



```python
import itertools
heights = [int(input()) for i in range(9)]
cmb = []
cmb += itertools.combinations(heights, 7)

valid_combos = [sorted(list(i)) for i in cmb if sum(i)==100]

answer = valid_combos[0]
for i in range(len(answer)):
    print(answer[i])
```



#### 2605. 줄 세우기

```python
N = int(input())
order = map(int,input().split())
result = []
for idx, value in enumerate(order):
    if idx == 0:
        result.append(idx+1)
    else:
        if value == 0:
            result.append(idx+1)
        else:
            pos = -1 - value +1
            result.insert(pos,idx + 1)

print(*result)



```



#### 2563. 색종이

```python
N = int(input())
arr = []
for i in range(100):
    temp = [0] * 100
    arr.append(temp)

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            arr[i][j] += 1

original_area = N * 100

count = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] >= 1:
            count += 1

print(count)
```



#### 2564. 경비원

```python
c, r = map(int, input().split())
num_of_stores = int(input())
store_location = []
for i in range(num_of_stores):
    store_location.append(list(map(int, input().split())))

my_location = list(map(int,input().split()))

if my_location[0] == 1:
    my_pos = [0, my_location[1]]

elif my_location[0] == 2:
    my_pos = [r, my_location[1]]

elif my_location[0] == 3:
    my_pos = [my_location[1], 0]

elif my_location[0] == 4:
    my_pos = [my_location[1], c]


total = 0
for each in store_location:
    if each[0] == 1:
        store_pos = [0, each[1]]
        if my_pos[0] == r:
            one = my_pos[0] + my_pos[1] + store_pos[1]
            two = my_pos[0] + c-my_pos[1] + c- store_pos[1]
            if one>two:
                total += two
            else:
                total += one
        else:
            total += abs(my_pos[0]-store_pos[0]) + abs(my_pos[1]-store_pos[1])


    elif each[0]== 2:
        store_pos = [r, each[1]]
        if my_pos[0] == 0:
            one = store_pos[0] + my_pos[1] + store_pos[1]
            two = store_pos[0] + c - my_pos[1] + c - store_pos[1]
            if one > two:
                total += two
            else:
                total += one
        else:
            total += abs(my_pos[0] - store_pos[0]) + abs(my_pos[1] - store_pos[1])


    elif each[0] == 3:
        store_pos = [each[1],0]
        total += abs(my_pos[0] - store_pos[0]) + abs(my_pos[1] - store_pos[1])

    elif each[0]==4:
        store_pos = [each[1],c]
        total += abs(my_pos[0] - store_pos[0]) + abs(my_pos[1] - store_pos[1])

print(total)

```

```python
def convert(col,row,direc,dis):
    p=dis
    if direc==2:
        p=2*col+row-dis
    if direc==3:
        p=2*(col+row)-dis
    if direc==4:
        p+=col
    return p
col, row=map(int, input().split())
N=int(input())
stores=[]
for _ in range(N):
    direc,dis= list(map(int,input().split()))
    p=convert(col,row,direc,dis)
    stores.append(p)
dong_dir, dong_dis=map(int,input().split())
dong=convert(col,row,dong_dir,dong_dis)
total=0
for i in range(N):
    a=abs(stores[i]-dong)
    b=2*(col+row)-a
    total+=min(a,b)
print(total)
```





#### 2491. 수열

```python
N = int(input())
nums = list(map(int, input().split()))

count = 1
countings = []

if N == 1:
    print(1)
else:
    increasing = True
    for i in range(N-1):
        if nums[i+1] >= nums[i]:
            if increasing:
                count += 1
        else:
            countings.append(count)
            count = 1
        if i == len(nums)-2:
            countings.append(count)
    
    decreasing = True
    for i in range(N-1):
        if nums[i+1] <= nums[i]:
            if decreasing:
                count += 1
        else:
            countings.append(count)
            count = 1
        if i == len(nums)-2:
            countings.append(count)
    
    
    print(max(countings))

```

