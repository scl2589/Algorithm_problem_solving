from collections import deque
def solution(arrangement):
    stack = 0
    answer = 0
    for index, i in enumerate(arrangement):
        if i == ')': #rasor 닫는 괄호
            stack -= 1
            if arrangement[index-1] == ')': #rasor 다음 닫는 괄호
                answer += 1
            else:
                answer += stack
            
        else:
            stack += 1
    
    return answer