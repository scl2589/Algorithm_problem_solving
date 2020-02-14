from collections import deque

T = int(input())

for tc in range(1, T+1):
    stack = deque()
    words = list(input())
    for i in words:
        if i not in stack:
            stack.append(i)
        else:
            if stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
    print('#{} {}'.format(tc, len(stack)))
        