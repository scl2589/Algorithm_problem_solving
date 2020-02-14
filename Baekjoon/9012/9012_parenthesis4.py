'''
1. '('가 나오면 스택에 '('를 넣어줌
2. ')'가 나오면, 스택에서 '('를 빼줌
- 스택이 비어있는지
-- 안비어있다면 --> pop()
-- 비어있다면 --> False
- stack이 비어있다면 --> True
- stack이 비어있지 않다면 --> False
'''
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    D = list(sys.stdin.readline().strip())
    stack = 0
    for p in D:
        if p == '(':
            stack += 1
        else:
            stack -=1
        if stack < 0:
            print('NO')
            break
    else:
        if stack:
            print('NO')
        else:
            print('YES')