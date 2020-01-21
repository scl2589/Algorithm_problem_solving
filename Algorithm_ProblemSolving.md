# 알고리즘 문제풀이

## Difficulty 1

### 2072. 홀수만 더하기

10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

[제약 사항] 

각 수는 0 이상 10000 이하의 정수이다.

[입력]

가장 첫 줄에는 테스트 케이스의 개수  T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```python
trial=int(input())
i=1
while i <= trial:
    numbers = input().split(' ')
    sum = 0
    for j in numbers:
        if int(j) % 2:
            sum += int(j)
    print("#{0} {1}".format(i, sum))
    i+=1
```





### 2071. 평균값 구하기

10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

(소수점 첫째 자리에서 반올림한 정수를 출력한다.)

[제약 사항]

각 수는 0 이상 10000 이하의 정수이다

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

[출력]

출력의 각 줄은 # t로 시작하고, 공백을 한 칸 둔 정답을 출력한다.

(t은 테스트 케이스의 번호를 의미하여 1부터 시작한다. )

```python
trial=int(input())
i=1
while i <= trial:
    numbers = input().split(' ')
    sum = 0
    count = 0
    for j in numbers:
        if int(j) % 2:
            sum += int(j)
            count += 1
    print("#{0} {1}".format(i, sum/count))
    i+=1
    
```



### 2070. 큰 놈, 작은 놈, 같은 놈

2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

[제약 사항]

각 수는 0 이상 10000 이하의 정수이다

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

[출력]

출력의 각 줄은 # t로 시작하고, 공백을 한 칸 둔 정답을 출력한다.

(t은 테스트 케이스의 번호를 의미하여 1부터 시작한다. )



```python
trial = int(input())
i = 1
while i <= trial:
    a,b = map(int,input().split())
    if a > b:
        print("#{0} >".format(i))
    elif a==b:
        print("#{0} =".format(i))
    else:
        print("#{0} <".format(i))
    i += 1
```



### 2068. 최대수 구하기

10개의 수를 입력 받아,  그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.

[제약 사항]

각 수는 0 이상 10000 이하의 정수이다

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

[출력]

출력의 각 줄은 # t로 시작하고, 공백을 한 칸 둔 정답을 출력한다.

(t은 테스트 케이스의 번호를 의미하여 1부터 시작한다. )

```python
trial = int(input())
i = 1
while i <= trial:
    numbers = map(int,input().split(' '))
    max=0
    for j in numbers:
        if j >= max:
            max = j
    print("#{0} {1}".format(i, max))
    i += 1
```





### 2063. 중간값 찾기

중간값은 통계 집단의 수치를 크기 순으로 배열했을 때 전체의 중앙에 위치하는 수치를 뜻한다.

입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.

[예제]

N이 9이고, 9개의 점수가 아래와 같이 주어질 경우,

85 72 38 80 69 65 68 96 22

69이 중간값이 된다.

[제약 사항]

1. N은 항상 홀수로 주어진다.
2. N은 9 이상 199이하의 정수이다. (9 ≤ N ≤ 199)

[입력]

입력은 첫 줄에 N이 주어진다.

둘째 줄에 N개의 점수가 주어진다.

[출력]

N개의 점수들 중, 중간값에 해당하는 점수를 정답으로 출력한다.

```python
while True:
    number = int(input())
    if number >= 9 and number <= 199:
        if number % 2 :
            break
numbers = list(map(int, input(). split(' ')))
numbers2 = sorted(numbers)
print(numbers2[len(numbers2)//2])
```



### 2058. 자릿수 더하기

하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라

[제약 사항]

자연수 N은 1부터 9999까지의 자연수이다. (1 <= N <= 9999)

[입력]

입력으로 자연수 N이 주어진다.

[출력]

각 자릿수의 합을 출력한다.

```python
number = input()
sum = 0
for i in number:
    sum += int(i)
print(sum)
```



### 2056. 연월일 달력

연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.

** 그림1 ** 22220228 -> 2222/02/28

해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면 [그림1]과 같이 "YYYY/MM/DD"형식으로 출력하고, 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.

연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며

일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.

단, 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 온다.

다음줄부터 각 테스트 케이스가 주어진다.

[출력]

출력의 각 줄은 # t로 시작하고, 공백을 한 칸 둔 정답을 출력한다.

(t은 테스트 케이스의 번호를 의미하여 1부터 시작한다. )

```python
trial = int(input())
i = 1
while i <= trial:
    date = input()
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])
    if month >= 1 and month <= 12:
        if month==1 or month == 3 or month == 5or month == 7 or month == 8 or month == 10 or month == 12:
            if day>=1 and day<=31:
                print("#{0} {1}/{2}/{3}".format(i,year, month, day ))
        elif month == 2:
            if day>=1 and day <= 28:
                print("#{0} {1}/{2}/{3}".format(i,year, month, day ))
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day>=1 and day<=30:
                print("#{0} {1}/{2}/{3}".format(i,year, month, day ))
        else:
            print('-1')
    else:
        print('-1')
            
        
    i += 1
```



### 2050. 알파벳을 숫자로 변환





### 2047. 신문 헤드라인





### 2046. 스탬프 찍기







