from collections import Counter
#collections 라이브러리의 Counter 함수를 사용한다.
N = int(input())
num1 = list(map(int, input().split()))
M = int(input())
num2 = list(map(int, input().split()))

C = Counter(num1)
for i in num2:
    print(C[i], end=' ')