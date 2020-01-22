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
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day >= 1 and day <= 31:
                print("#{0} {1}/{2}/{3}".format(i, date[0:4], date[4:6], date[6:8]))
            else:
                print("#{0} -1".format(i))
        elif month == 2:
            if day >= 1 and day <= 28:
                print("#{0} {1}/{2}/{3}".format(i, date[0:4], date[4:6], date[6:8]))
            else:
                print("#{0} -1".format(i))
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day >= 1 and day <= 30:
                print("#{0} {1}/{2}/{3}".format(i, date[0:4], date[4:6], date[6:8]))
            else:
                print("#{0} -1".format(i))
        else:
            print("#{0} -1".format(i))
    else:
        print("#{0} -1".format(i))
    i += 1
```



### 2050. 알파벳을 숫자로 변환

알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.

[제약 사항]

문자열의 최대 길이는 200이다.

[입력]

알파벳으로 이루어진 문자열이 주어진다.

[출력]

각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.

```python
letters = input()
for letter in letters:
    print(ord(letter)-64, end = ' ')
```



### 2047. 신문 헤드라인

신문의 헤드라인을 편집하기 위해, 주어지는 문자열의 알파벳 소문자를 모두 대문자로 바꾸는 프로그램을 개발 중이다. 입력으로 주어진 문장에 모든 소문자 알파벳을 찾아 대문자로 변환한 다음, 그 결과를 출력하는 프로그램을 작성하라.

**[예제 풀이]**

The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.

위와 같은 문자열이 입력으로 주어졌을 때, 출력은 다음과 같다.

THE_HEADLINE_IS_THE_TEXT_INDICATING_THE_NATURE_OF_THE_ARTICLE_BELOW_IT.


**[제약 사항]**

문자열의 최대 길이는 80 bytes 이다.


**[입력]**

입력으로 80 bytes 이하의 길이를 가진 문자열이 주어진다.


**[출력]**

문자열의 소문자를 모두 대문자로 변경한 결과를 출력한다.

```python
sentence=input()
print(sentence.upper())
```



### 2046. 스탬프 찍기

주어진 숫자만큼 # 을 출력해보세요.

주어질 숫자는 100,000 이하다.

```
num=int(input())
print('#' * num)
```



### 2043. 서랍의 비밀번호

서랍의 비밀번호가 생각이 나지 않는다.

비밀번호 P는 000부터 999까지 번호 중의 하나이다.

주어지는 번호 K부터 1씩 증가하며 비밀번호를 확인해 볼 생각이다.

예를 들어 비밀번호 P가 123 이고 주어지는 번호 K가 100 일 때, 100부터 123까지 24번 확인하여 비밀번호를 맞출 수 있다.

P와 K가 주어지면 K부터 시작하여 몇 번 만에 P를 맞출 수 있는지 알아보자.


**[입력]**

입력으로 P와 K가 빈 칸을 사이로 주어진다.


**[출력]**

몇 번 만에 비밀번호를 맞출 수 있는지 출력한다.



```python
p, k = map(int,input().split(' '))
count = 0
for i in range(k, p+1):
    count += 1
print(count)

```



### 2029. 몫과 나머지 출력하기

2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

**[제약 사항]**

각 수는 1이상 10000이하의 정수이다.


**[입력]**

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.


**[출력]**

출력의 각 줄은 '#t'로 시작하고 공백을 한 칸 둔 다음, 몫을 출력하고 공백을 한 칸 둔 다음 나머지를 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)



```python
trial = int(input())
for i in range(trial):
    a, b = map(int,input().split(' '))
    dividing=divmod(a,b)
    print('#{0} {1} {2}'.format(i+1, dividing[0], dividing[1]))
```



### 2027. 대각선 출력하기

주어진 텍스트를 그대로 출력하세요.

\#++++
+#+++
++#++
+++#+
++++#

```python
print('#++++')
print('+#+++')
print('++#++')
print('+++#+')
print('++++#')
```



### 2025. N줄 덧셈

1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.

단, 주어질 숫자는 10000을 넘지 않는다.


**[예제]**

주어진 숫자가 10 일 경우 출력해야 할 정답은,

1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

```python
number = int(input())
total = 0
for i in range(1, number+1):
    total += i
    if i == number:
        print('{0} = {1}'.format(i,total))
    else:
        print('{} + '.format(i),end='')
```

```python
number = int(input())
total = 0
for i in range(1, number+1):
    total += i

print(total)
```



### 1938. 아주 간단한 계산기

두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성하라.

 

**[제약 사항]**

\1. 두 개의 자연수 a, b는 1부터 9까지의 자연수이다. (1 ≤ a, b ≤ 9)

\2. 사칙연산 + , - , * , / 순서로 연산한 결과를 출력한다.

\3. 나누기 연산의 결과에서 소수점 이하의 숫자는 버린다.

**[입력]**

입력으로 두 개의 자연수 a, b가 빈 칸을 두고 주어진다.

**[출력]**

사칙연산의 결과를 각 줄에 순서대로 출력한다.

```python
b, c = map(int, input().split(' '))
print(b+c)
print(b-c)
print(b*c)
print(b//2)

```



### 1933. 간단한 N의 약수

입력으로 1개의 정수 N 이 주어진다.

정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

**[제약사항]**

N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)

**[입력]**

입력으로 정수 N 이 주어진다.
**[출력]**

정수 N 의 모든 약수를 오름차순으로 출력한다.

```python
num = int(input())
factor = []
for i in range(1, num+1):
    if num % i == 0 :
        factor.append(i)

for j in sorted(factor):
    print(j,end=' ')
```



### 1936. 1대1 가위바위보

A와 B가 가위바위보를 하였다.

가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.

A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.

**[입력]**

입력으로 A와 B가 무엇을 냈는지 빈 칸을 사이로 주어진다.

**[출력]**

A가 이기면 A, B가 이기면 B를 출력한다.

```python
a, b = map(int,input().split(' '))
if a==1:
    if b==2:
        print('B')
    else:
        print('A')
elif a==2:
    if b==1:
        print('A')
    else:
        print('B')
else:
    if b==1:
        print('B')
    else:
        print('A')

```



### 2019. 더블더블

1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

주어질 숫자는 30을 넘지 않는다.

```python
trial=int(input())
for i in range(0,trial+1):
    print(2**i,end=' ')
```



### 1545. 거꾸로 출력해 보아요

주어진 숫자부터 0까지 순서대로 찍어보세요

아래는 입력된 숫자가 N일 때 거꾸로 출력하는 예시입니다

```python
num = int(input())
for i in range(num,-1,-1):
    print(i, end=' ')

```





## Difficulty 2