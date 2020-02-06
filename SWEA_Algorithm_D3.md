## Difficulty 3

### 7675. 통역사 성경이

```python
trial = int(input())
for tc in range(1, trial + 1):
    n = int(input())
    sentences = input()
    separated = []
    temp = ''
    scoreboard = []

    for letter in sentences:
        if letter == '!' or letter == '.' or letter == '?':  # 만약 !, ?, .이 보인다면
            # 각각의 글자를 임시 str에 넣어놓고, #separated list 에 넣어놓자
            separated.append(temp)
            temp =''
        else:
            temp += letter  # 아니라면 temp 스트링에 넣어놓자

    for sentence in separated:  # 구별된 문장마다
        score = 0
        words = list(sentence.strip().split(' '))  # 각 단어를 띄어쓰기 별로 구분하자.

        for word in words: #단어별로 계산하자.
            count = 0

            for idx in range(len(word)):  # 각 단어의 첫글자 빼고 모두 소문자인지 확인하자.
                if idx == 0:
                    if word[0].isupper():
                        count +=1

                else:
                    if word[idx].islower():
                        count+=1

            if count == len(word):
                score += 1
        scoreboard.append(score)

    print(f'#{tc}', " ".join(map(str,scoreboard)))
```



### 6692. 다솔이의 월급 상자

```python
trial = int(input())
for tc in range(trial):
    n = int(input())
    total = 0
    for i in range(n):
        p, x = map(float, input().split(' '))
        total += p * x

    print('#{0} {1}'.format(tc+1,total))
```



### 1206. View

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



### 5601. 쥬스 나누기

```python
trial = int(input())
for tc in range(1, trial + 1):
    n = int(input())
    result = []
    for _ in range(n):
        result.append('1/'+str(n))

    print('#{} {}'.format(tc, ' '.join(result)))
```



### 5603. 건초더미

```python
trial = int(input())
for tc in range(1, trial + 1):
    n = int(input())
    size = []
    ans = 0

    for _ in range(n):
        size.append(int(input()))

    average = sum(size)/n

    for eachsize in size:
        ans += abs(average - eachsize)
    ans = int(ans//2)
    print('#{} {}'.format(tc, ans))
```



-----

### 1208. Flatten

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



### 1215. 회문1

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





### 4715. 다솔이의 다이아몬드 장식

```python
trial = int(input())
for tc in range(1, trial + 1):
    words = input()
    length = len(words) * 4 + 1

    for i in range(5):
        sentence = ''

        if i == 0 or i == 4:
            for j in range(1, length + 1):
                if j % 4 == 3:
                    sentence += '#'
                else:
                    sentence += '.'
            print(sentence)

        if i == 1 or i == 3:
            for j in range(length):
                if j % 2:
                    sentence += '#'
                else:
                    sentence += '.'
            print(sentence)

        if i == 2:
            for k in range(1, length + 1):
                if k % 4 == 1:
                    sentence += '#'
                elif k % 2 ==0:
                    sentence += '.'
                elif k % 4 == 3:
                    sentence += words[(k - 3) // 4]

            print(sentence)
```



### 4406. 모음이 보이지 않는 사람

```python
trial =  int(input())
for tc in range(1, trial+1):
    word = input()
    vowels = 'aeiou'
    result=''
    for letter in word:
        if letter not in vowels:
            result += letter
    print('#{} {}'.format(tc, result))
            
```



### 3431. 준환이의 운동관리

```python
trial = int(input())
for tc in range(1,trial+1):
    l, u, x = map(int, input().split())
    if l <= x <= u:
        print('#{} 0'.format(tc))
    elif x< l and x < u:
        print('#{} {}'.format(tc, l-x))
    elif x > l and x > u:
        print('#{} -1'.format(tc))
```



### 3314. 보충학습과 평균

```python
trial = int(input())
for tc in range(1, trial+1):
    scores = list(map(int, input().split()))
    total = 0
    for score in scores:
        if score < 40:
            total += 40
        else:
            total += score
    average = total//len(scores)
    print('#{} {}'.format(tc, average))

```





### 1860. 진기의 최고급 붕어빵

```python
trial = int(input())
for tc in range(1, trial + 1):
    n, m, k = map(int, input().split())
    arrivaltime = list(map(int, input().split()))
    arrivaltime.sort()

    bread = 0
    answer = True

    for each in arrivaltime:
        if each < m:
            answer = False
            break

    for i in range(0, max(arrivaltime)+1):
        if answer == False:
            break
        # m초마다 k개의 붕어빵을 생성한다.
        elif i != 0 and i % m == 0:
            bread += k
            #이 시간까지시간에 방문한 손님 수 만큼 븡어빵 수 감소
            if i in arrivaltime:
                bread -= 1;
        elif i!= 0 and i > m:
             if i in arrivaltime:
                bread -= 1

        if bread < 0:
            answer = False
            break

    if answer == True:
        result = 'Possible'
    else:
        result = 'Impossible'
        
    print('#{} {}'.format(tc, result))

```



### 1289. 원재의 메모리 복구하기

```python
trial = int(input())
for tc in range(1, trial+1):
    n = input()
    current = '0'
    count = 0
    for i in range(len(n)):
        if n[i] != current:
            count += 1
            current = n[i]
           
    print('#{} {}'.format(tc, count))
```



### 1234. 비밀번호

```python
# import sys

# sys.stdin = open('input.txt')
for tc in range(1, 11):
    N, numbers = input().split()
    nums = []
    for n in numbers:
        nums.append(n)

    while True:
        count = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                del nums[i:i+2]
                count += 1
                break
        if count == 0:
            break

    print('#{} {}'.format(tc,''.join(nums)))

```



### 1230. 암호문3

```python
for tc in range(1, 11):
    lenofpw = int(input())
    passwords = list(map(str, input().split()))
    lenofcmd = int(input())
    commands = list(map(str, input().split()))

    for i in range(len(commands)):
        if commands[i] == 'I':
            # 추가를 해야할 숫자 (숫자 다음에 추가) , 숫자 삽입 개수, 삽입해야할 숫자 받기
            location = int(commands[i + 1]) 
            numsofcmd = int(commands[i + 2])

            # 암호에 숫자 삽입하기
            for u in range(numsofcmd):
                passwords.insert(location + u, commands[i + 3 + u])

        # 삭제를 해야할 숫자 (숫자 다음부터 삭제) , 삭제 개수 받기
        elif commands[i] == 'D':
            location = int(commands[i + 1]) 
            numstodel = int(commands[i + 2])

            # 암호 숫자 삭제하기
            for i in range(numstodel):
                # del passwords[location: location + numstodel]
                del passwords[location]

                # 맨 뒤에 붙일 숫자 개수, 덧붙일 숫자 받기
        elif commands[i] == 'A':
            numsofcmd = int(commands[i + 1])

            # 암호 끝에 숫자 더하기
            for u in range(numsofcmd):
                passwords.append(commands[i + 2 + u])

            # passwords.append(numstoadd)
    print('#{} {}'.format(tc, ' '.join(passwords[:10])))

```



### 1228. 암호문1

```python
for tc in range(1, 11):
    lenofpw = int(input())
    passwords = list(map(str, input().split()))
    lenofcmd = int(input())
    commands = list(map(str, input().split()))

    for i in range(len(commands)):
        if commands[i] == 'I':
            # 추가를 해야할 숫자 (숫자 다음에 추가) , 숫자 삽입 개수, 삽입해야할 숫자 받기
            location = int(commands[i + 1])
            numsofcmd = int(commands[i + 2])
            numstoinsert = commands[i + 3: i + 3 + int(numsofcmd)]

            #암호에 숫자 삽입하기
            for j in range(numsofcmd):
                 passwords.insert(location + j, commands[i+3+j])
    passwords = ' '.join(passwords[:10])

    print('#{} {}'.format(tc, passwords))

```



### 1225. 암호생성기

```python
for tc in range(1, 11):
    tc = int(input())
    numbers = list(map(int, input().split()))
    count = 1
    mustcontinue = True
    while mustcontinue == True:
        numbers[0] -= count
        count += 1
        if numbers[0] <= 0:
            numbers[0] = 0
            numbers.append(numbers[0])
            del numbers[0]
            mustcontinue = False
        else:
            numbers.append(numbers[0])
            del numbers[0]
            if count == 6:
                count = 1
    numbers= list(map(str, numbers))
    numbers = ' '.join(numbers)

    print('#{} {}'.format(tc, numbers))
```



### 1217. 거듭 제곱

```python
def power(x,y):
    return x * power(x,y-1) if y !=0 else 1
        
for tc in range(1, 11):
    t = int(input())
    n, m = map(int, input().split())
    print('#{} {}'.format(tc, power(n,m)))
    
```



### 1213. String

```python
for tc in range(1, 11):
    trial = int(input())
    need_to_find = input()
    sentence = input()
    count = 0
    for j in range(0,len(sentence)-len(need_to_find)+1):
        if need_to_find == sentence[j:j+len(need_to_find)]:
            count += 1
    print('#{} {}'.format(tc,count))
```



### 1209. Sum

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



### 4047. 영준이의 카드 카운팅

```python
trial = int(input())
for tc in range(1, trial+1):
    card = input()
    cards = []
    for each in range(0, len(card),3):
        cards.append(card[each:each+3])
    if len(cards) != len(set(cards)):
        print('#{} ERROR'.format(tc))
    else:
        count = [13, 13, 13, 13] #S, D, H, C
        for each in cards:
            if each[0]=='S':
                count[0] -= 1
            elif each[0]=='D':
                count[1] -= 1
            elif each[0]=='H':
                count[2] -= 1
            else:
                count[3] -= 1
        print('#{} {}'.format(tc, ' '.join(map(str,count))))


```





### 6190. 정곤이의 단조 증가하는 수

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

```python
#수민오빠 버전
T = int(input())
for case in range(1,T+1):
    N = input()
    A = input().split()
    result = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            s = str(int(A[i]) * int(A[j]))
            count = 1
            for k in range(len(s)-1):
                if s[k] > s[k+1]:
                    count = 0
                    break
            if count == 1:
                if result < int(s):
                    result = int(s)
    if result == 0:
        result = -1
    print('#{} {}'.format(case, result))

```



### 2805. 농작물 수확하기

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



### 5607. 조합

```python
ㅇ
```



### 5607. 조합

```python
ㅇ
```





### 5607. 조합

```python
ㅇ
```





### 5607. 조합

```python
ㅇ
```





### 5607. 조합

```python
ㅇ
```



