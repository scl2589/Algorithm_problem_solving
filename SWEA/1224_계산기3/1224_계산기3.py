def get_weight(operator):
    if operator == '*':
        return 9
    elif operator == '+':
        return 7
    elif operator == '(':
        return 5
    else:
        return -1

for tc in range(1, 11):
    N = int(input())
    equation = list(input())
    digit = []
    stack = []
    #후기 표기법으로 바꾸기
    for i in equation:
        #숫자라면
        if i.isdigit():
            digit.append(i)
        #연산자라면
        else:
            if i == '(' or not stack:
                stack.append(i)
            elif i == ')':
                token = stack.pop()
                while token != '(':
                    digit.append(token)
                    token = stack.pop()
            #'+'이거나 '*'일 때
            else:
                current_weight = get_weight(i)
                top_weight = get_weight(stack[-1])
                if current_weight > top_weight:
                    stack.append(i)
                elif current_weight <= top_weight:
                    while stack and current_weight <= top_weight:
                        digit.append(stack.pop())
                        if stack:
                            top_weight = get_weight(stack[-1])
                    stack.append(i)
    while stack:
        digit.append(stack.pop())
    numbers = []
    #후기 표기법의 수식을 스택을 이용하여 계산하자
    for i in digit:
        if i.isdigit():
            numbers.append(i)
        else:
            a = int(numbers.pop())
            b = int(numbers.pop())
            if i == '*':
                numbers.append(a * b)
            elif i == '+':
                numbers.append(a + b)
    print('#{} {}'.format(tc, *numbers))
