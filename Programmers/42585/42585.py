from collections import deque
def solution(arrangement):
    answer = 0
    stack = deque()
    count = 0
    for i in arrangement:
        if i == '(':
            stack.append(i)
        else:
            if stack[-1] == i:
                if len(stack) > 2:
                    count += 1
                stack.pop()
            else:
                answer += len(stack) * (count+1)
                count = 0
            
    
    return answer