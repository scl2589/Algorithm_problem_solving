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



### 1984. 중간 평균값 구하기

```python

```





### 1983. 조교의 성적 매기기

```python

```



### 1979. 어디에 단어가 들어갈 수 있을까

```python

```



### 1976. 시각 덧셈

```python

```



### 1974. 스도쿠 검증

```python

```





### 1970. 쉬운 거스름돈

```python

```





### 1966. 숫자를 정렬하자

```python

```





### 1961. 숫자 배열 회전

```python

```







### 1959. 두 개의 숫자열

```python

```







### 1954. 달팽이 숫자

```python

```







### 1948. 날짜 계산기

```python

```







### 1946. 간단한 압축 풀기

```python

```







### 1945. 간단한 소인수분해

```python

```





### 1940. 가랏! RC카!

```python

```



### 1928. Base64 Decoder

```python

```







### 1288. 새로운 불면증 치료법

```python

```





### 1284. 수도 요금 경쟁

```python

```





### 1204. 최빈수 구하기

```python

```



