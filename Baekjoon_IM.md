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
#dices = [list(map(int, input().split())) for _ in range(num)]
dices = []
for _ in range(num):
    temp = list(map(int, input().split()))
    dictionary = {}
    for i in range(6):
        if i == 0 :
            dictionary[temp[0]]=temp[5]
        elif i == 1:
            dictionary[temp[1]]=temp[3]
        elif i == 2:
            dictionary[temp[2]]=temp[4]
        elif i == 3:
            dictionary[temp[3]]=temp[1]
        elif i == 4:
            dictionary[temp[4]]=temp[2]
        else:
            dictionary[temp[5]]=temp[0]
        dices.append(dictionary)

result = []
#6개 각각의 베이스
for i in range(1, 7):
    base = dices[0][i]
    for idx, value in enumerate(dices):
        ref = [1, 2, 3, 4, 5, 6]
        for j in range(1, 7):
            ref.remove(base)
            
            #다음 베이스가 된당!
            #base = value.get(i)

            ref.remove(i)
            side = max(ref)
            result.append(side)
    #else:




#base가 될 수 있는 6가지 경우를 살펴본다.
# result = []
# for i in range(6):
#     total = []
#     base = dices[0][i]
#     ref = [1,2,3,4,5,6]
#     if i == 0 or i == 5:
#         ref.remove(dices[0][0])
#         ref.remove(dices[0][5])
#     elif i == 2 or i == 4:
#         ref.remove(dices[0][2])
#         ref.remove(dices[0][4])
#     else:
#         ref.remove(dices[0][1])
#         ref.remove(dices[0][3])
#     first_side = max(ref)
#     total.append(first_side)
#     j = 1
#     while j < num:
#         temp = 0
#         for k in range(6):
#             if base == dices[j][k]:
#                 ref = [1, 2, 3, 4, 5, 6]
#                 if k == 0 or k == 5:
#                     if k == 0:
#                         base = dices[j][5]
#                     else:
#                         base = dices[j][0]
#                     ref.remove(dices[j][0])
#                     ref.remove(dices[j][5])
#
#                 elif k == 2 or k == 4:
#                     if k == 2:
#                         base = dices[j][4]
#                     else:
#                         base = dices[j][2]
#                     ref.remove(dices[j][2])
#                     ref.remove(dices[j][4])
#                 else:
#                     if k == 1:
#                         base = dices[j][3]
#                     else:
#                         base = dices[j][1]
#                     ref.remove(dices[j][1])
#                     ref.remove(dices[j][3])
#                 temp = max(ref)
#         total.append(temp)
#         j += 1
#     result.append(total)
#     i+=1
#
# final = 0
# for i in result:
#     if sum(i) > final:
#         final = sum(i)
#
# print(final)
```



#### 2304. 창고 다각형

```python

```



#### 2559. 수열

```python

```



#### 2578. 빙고

```python

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

```



#### 13300. 방 배정

```python

```



#### 14696. 딱지놀이

```python

```



#### 2309. 일곱 난쟁이

```python

```



#### 2605. 줄 세우기

```python

```



#### 2563. 색종이

```python

```



#### 2564. 경비원

```python

```



#### 2491. 수열

```python

```

