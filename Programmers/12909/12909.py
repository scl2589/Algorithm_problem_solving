from collections import deque
def solution(s):
    stack = deque()
    answer = True
    
    lists = list(s)
    for i in lists:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack)!=0:
                stack.pop()
            else:
                answer = False
                break
    if len(stack)!=0:
        answer = False
    return answer