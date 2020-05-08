#시간초과가 난다.
"""
N = int(input())
num1 = list(map(int, input().split()))
M = int(input())
num2 = list(map(int, input().split()))


for target in num2:
    count = 0
    for num in num1:
        if num == target:
            count += 1
    print(count, end=" ")
"""

#dict를 사용한다.
N = int(input())
num1 = list(map(int, input().split()))

dict = {}
for num in num1:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

M = int(input())
num2 = list(map(int, input().split()))

answer = []
for num in num2:
    if num in dict:
        print(str(dict[num]), end=' ')
    else:
        print(0, end=' ')