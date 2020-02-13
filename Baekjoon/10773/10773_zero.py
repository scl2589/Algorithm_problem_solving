'''
재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 
가장 최근에 재민이가 쓴 수를 지우게 시킨다.
재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 
재민이를 도와주자!
'''
from collections import deque

K = int(input())
stack = deque()
for i in range(K):
    num = int(input())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))