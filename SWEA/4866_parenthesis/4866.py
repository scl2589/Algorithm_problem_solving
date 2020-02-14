'''
주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.
'''
from collections import deque

T = int(input())
for tc in range(1, T+1):
    stack = deque()
    lines = list(input())
    answer= True
    for i in lines:
        if i == '{' or i== '(':
            stack.append(i)
        elif i == '}' :
            if len(stack)!= 0:
                taken_out = stack.pop()
                if taken_out != '{':
                    answer= False
            else:
                answer = False
        elif i==')':
            if len(stack)!= 0:
                taken_out = stack.pop()
                if taken_out != '(':
                    answer= False
            
            else:
                answer = False
    if answer == True and len(stack)==0:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
        
