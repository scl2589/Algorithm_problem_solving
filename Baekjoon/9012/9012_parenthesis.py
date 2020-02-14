from collections import deque

T = int(input())
for tc in range(1, T+1):
    stack = deque()
    parenthesis = list(input())
    answer = True
    for i in parenthesis:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                answer = False
            else:
                stack.pop()
    if answer == True and len(stack) == 0:
        print('YES')
    else:
        print('NO')

    
    