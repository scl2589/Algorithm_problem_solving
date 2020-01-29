## Difficulty 3

### 1926. 간단한 369게임

3 6 9 게임을 프로그램으로 제작중이다. 게임 규칙은 다음과 같다.

 

\1. 숫자 1부터 순서대로 차례대로 말하되, **“3” “6” “9”** 가 들어가 있는 수는 말하지 않는다.

 **1 2** **3** **4 5** **6** **7 8** **9…**

\2. "3" "6" "9"가 들어가 있는 수를 말하지 않는대신, 박수를 친다. 이 때, 박수는 해당 숫자가 들어간 개수만큼 쳐야 한다. 
예를 들어 숫자 35의 경우 박수 한 번, 숫자 36의 경우 박수를 두번 쳐야 한다.

입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를

게임 규칙에 맞게 출력하는 프로그램을 작성하라.

박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.

**여기서 주의해야 할 것은 박수 한 번 칠 때는 - 이며, 박수를 두 번 칠 때는 - - 가 아닌 -- 이다. 


** 

**[제약사항]**

N은 10이상 1,000이하의 정수이다. (10 ≤ N ≤ 1,000)

**[입력]**

입력으로 정수 N 이 주어진다.

**[출력]**

1 ~ N까지의 숫자를 게임 규칙에 맞게 출력한다.



```python
num = int(input())

for i in range(1, num+1):
    count = 2
    for j in str(i):
        if int(j) > 0 :
            if int(j) % 3 == 0:
                count -= 1
    if count == 0:
        print('--',end=' ')
    elif count==1 :
        print('-', end= ' ')
    else :
        print(i, end = ' ')


```



### 2007. 패턴 마디의 길이



```python
trial = int(input())
for i in range(trial):
    string = input()
    words = ''
    answer= ''
    for idx in range (0, 30, 2):
        words += string[ idx : idx+2]
        num=len(words)//2
        if words[:num]==words[num:]:
            answer += words[:num]
            break
    print(f'#{i+1} {len(answer)}')
            
```



### 2005. 파스칼의 삼각형

```python
trial = int(input())

for i in range(0, trial):
    height = int(input())
    prev_dict = [1, 1]
    print(f'#{i+1}')
    for j in range (0, height):
        if j  ==  0:
            print('1')
        elif j  ==  1:
            print('1 1')
        elif j >=  2:
            new_dict= [1]      
            for idx in range(1, j):
                sum = prev_dict[idx-1] + prev_dict[idx]        
                new_dict.append(sum)
            new_dict.append(1)
            print(*new_dict)
            prev_dict = new_dict
```





### 2001. 파리 퇴치

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



### 1989. 초심자의 회문 검사

```python
trial = int( input() )
for i in range(trial):
    word = input()
    reverse=''
    for letter in range(len(word)-1,-1,-1):
        reverse += word[letter]
    if reverse == word:
        print(f'#{i+1} 1')
    else:
         print(f'#{i+1} 0')
```





### 1986. 지그재그 숫자

```python
trial = int(input())
for i in range(trial):
    num = int(input())
    sum = 0 
    for number in range(1, num+1):
        if number % 2 == 1:
            sum += number
        else:
            sum -= number
    print(f'#{i+1} {sum}')
            
```



### 1984. 중간 평균값 구하기

```python
trial = int(input())
for i in range(trial):
    list1 = list(map(int, input().strip().split(' ')))
    list1.sort()
    list1.remove(min(list1))
    list1.remove(max(list1))
    result = format(round(sum(list1)/len(list1),0),".0f")
    print(f"#{i+1} {result}")
    
```





### 1983. 조교의 성적 매기기

```python
import math
trial = int(input())
for i in range(trial):
    students, studentnum = map(int, input().split(' '))
    list1=[]
    grade= ['D0','C-','C0','C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+'] 
    for _ in range(students):
        list1.append(list(map(int,input().strip().split(' '))))
    scores = []
    for j in range(students):       
        scores.append(list1[j][0]*0.35+list1[j][1]*0.4+list1[j][2]*0.2)
        scores.sort()

    idx = scores.index(list1[studentnum-1][0]*0.35+list1[studentnum-1][1]*0.4+list1[studentnum-1][2]*0.2)

    print(f'#{i+1} {grade[idx//((len(scores)//10)) ] }')

```



### 1979. 어디에 단어가 들어갈 수 있을까

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



### 1976. 시각 덧셈

```python
trial = int(input())
for i in range(trial):
    hours = list(map(int, input().strip().split(' ')))
    hour = 0
    minute = 0
    for idx in range(len(hours)):
        if idx % 2 == 0:
            hour += 60 * hours[idx]
        else:
            minute += hours[idx]
    total = hour + minute
    answerhour = total // 60
    if answerhour % 12 == 0 :
        answerhour = 12
    else:
        answerhour = answerhour % 12
    answerminute = total % 60
    print(f'#{i+1} {answerhour} {answerminute}')
    
```



### 1974. 스도쿠 검증

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





### 1970. 쉬운 거스름돈

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





### 1966. 숫자를 정렬하자

```python
trial = int(input())

for i in range(trial):
    n = int(input())
    numbers = []

    number = list(map(int, input().split(' ')))

    number.sort()

    print('#'+str(i+1),end= ' ')
    for i in number:
        print(i, end = ' ')
    print(' ')
    #print(f'#{i + 1} {result}')
```





### 1961. 숫자 배열 회전

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







### 1959. 두 개의 숫자열

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







### 1954. 달팽이 숫자

```python
def solve(n):
    direction_list = [(0,1), (1,0), (0,-1), (-1,0)] #Right, down, left, up
    num = 0
    direction_index = 0
    row, col = 0, -1

    array = [[-1] * n for i in range(n)]

    while num < n * n:
        direction = direction_list[direction_index]
        temp_row = row + direction[0]
        temp_col = col + direction[1]

        #범위가 초과되면 방향을 바꾸자.
        if temp_col < 0 or temp_row <0 or temp_col >= n or temp_row >= n or array[temp_row][temp_col] != -1:
            direction_index += 1
            if direction_index == 4:
                direction_index = 0
        else:
            num += 1
            row, col = temp_row, temp_col
            array[row][col] = num

    return array

trial = int(input())
for tc in range(trial):
    n = int(input())
    print(f'#{tc+1}')
    answer = solve(n)
    for line in answer:
        print(' '.join(map(str,line)))
```







### 1948. 날짜 계산기

```python
trial = int(input())
for i in range(trial):
    difference = 0

    calendar = {
        1 : 31,
        2 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31,
    }

    list1 = list(map(int, input().strip().split(' ')))

    if list1[0]==list1[2]:
        difference += list1[3] - list1[1] + 1
    else:
        difference += calendar[list1[0]]-list1[1]+1
        difference += list1[3]
        for month in range(list1[0]+1,list1[2]):
            difference += calendar[month]

    print(f'#{i+1} {difference}')

```







### 1946. 간단한 압축 풀기

```python
trial = int(input())
for i in range(trial):
    number = int(input())
    print(f'#{i+1}')
    list1 = []
    result = ''
    for _ in range(number):
        list1.append( list(map(str, input().strip().split(' '))) )
    for j in range(number):
        result += list1[j][0]*int(list1[j][1])
    for k in range(len(result)):
        if k>= 10 and k % 10 == 0:
            print('')
            print(result[k], end = '')
        else:
            print(result[k], end = '')
    print('')
```







### 1945. 간단한 소인수분해

```python
trial = int(input())
for i in range(trial):
    number = int(input())
    a=0
    b=0
    c=0
    d=0
    e=0
    for j in range(1000):
        if number % 2 ==0:
            a += 1
            number=number/2
        elif number % 3 == 0:
            b += 1
            number = number/3
        elif number % 5 == 0:
            c += 1
            number = number/5
        elif number % 7 ==0:
            d += 1
            number = number/7
        elif number % 11 ==0:
            e += 1
            number = number/11
        if number / 2 ==1:
            break
    print(f'#{i+1} {a} {b} {c} {d} {e}')

```





### 1940. 가랏! RC카!

```python
trial = int(input())
for i in range(1, trial + 1):
    command_num = int(input())
    list1 = []
    speed = 0
    distance = 0

    for j in range(command_num):
        list1.append(list(map(int, input().split(' '))))

    for k in range(len(list1)):

        if list1[k][0]==0: #0일때
            distance += speed
        elif list1[k][0]==1: #1일 때 (가속)
            speed += list1[k][1]
            distance += speed
        elif list1[k][0]==2: #2일 때 (감속)
            speed -= list1[k][1]
            if speed <= 0: #speed가 0 밑으로 내려간다면 0으로!
                speed = 0
            distance += speed

    print('#{0} {1}'.format(i, distance))


```



### 1928. Base64 Decoder

```python
trial = int(input())

for i in range(trial):
    phrase = input()
    encoded_bin = ''
    for word in phrase:
        #입력받은 글자 아스키로 변환하기 & 아스키를 2진수로 변환하기
        if word >= 'A' and word <= 'Z':
            char_to_bin = str(bin(ord(word)-65))
        elif word >= 'a' and word <= 'z':
            char_to_bin = str(bin(ord(word)-71))
        elif word >= '0' and word <= '9':
            char_to_bin = str(bin(ord(word) + 4))
        else:
            if word == '+':
                char_to_bin = str(bin(ord(word)+19))
            else:
                char_to_bin = str(bin(ord(word)+16))
        encoded_bin += "0"*(8-len(char_to_bin))+char_to_bin[2:]

    decoded_bin = []
    for j in range(0, len(encoded_bin), 8):
        chunk = encoded_bin[j:j+8]
        decoded_bin.append(chunk)

    decoded_char = [chr(int(bin,2)) for bin in decoded_bin]
    decoded_sentence = ''.join(decoded_char)

    print(f'#{i+1} {decoded_sentence}')

```



### 



### 1288. 새로운 불면증 치료법

```python
trial = int(input())
for trying in range(trial):
    seen = []
    num = int(input()) # int
    for i in range(1, 10**6+1):
        if len(seen) == 10:
            print('#{0} {1}'.format(trying+1, (i-1)*num))
            break         
        else:
            changenum = str(i*num)
            for x in changenum:
                if x not in seen:
                    seen.append(x)
            
```



### 

### 1284. 수도 요금 경쟁

```python
trial = int (input())
for trying in range(trial):
    P, Q, R, S, W = map(int, input().split(' '))
    a = P * W
    if W < R:
        b = Q
    else:
        b = Q+(W-R)*S
    if a < b:
        print("#{0} {1}".format(trying+1, a))
    else:
        print("#{0} {1}".format(trying+1, b))
       
    
                        
```



### 

### 1204. 최빈수 구하기

```python
trial = int(input())
for i in range(trial):
    j = int(input())
    list1 = []
    
    scores = list(map(int, input().strip().split(' ')))

    for _ in range(101):  # 0부터 100까지 0
        list1.append(0)
    for score in scores:  # 점수가 있다면 1 추가하기
        list1[score] += 1
	
    m = max(list1)
    list2 = [a for a, k in enumerate(list1) if k == m]
    maxnum = list2[-1]
    print(f'#{i + 1} {maxnum}')


```



### 