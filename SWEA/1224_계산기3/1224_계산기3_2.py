# 후위표기식
# - 스택 (LIFO) 필요
# - Infix 를 Postfix로 바꾸는 법
#   - 숫자를 만나면 그대로 출력
#   - 연산자를 만났을 때 스택이 비어있다면 스택에 push
#   - 괄호를 만났다면?
#     - 여는 괄호이면 스택에 push
#     - 닫는 괄호이면 스택에서 여는 괄호가 나올때까지 pop을 한 후 출력
#   - 연산자를 만났다면?
#     - 스택의 마지막 요소가 자기보다 우선순위가 낮은 연산자라면 pop을 한 후 출력
#     - 자신이 우선순위가 더 높다면 스택에 push
#   - 스택이 비어있지 않다면 계속해서 pop을 한 후 출력


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
    original = list(input())
    stack = []
    equation = []
    for i in original:
        # 숫자라면
        if i.isdigit():
            equation.append(i)
        else:
            # 스택이 비어있거나 여는 괄호라면
            if i == '(' or not stack:
                stack.append(i)
            # 닫는 괄호라면
            elif i == ')':
                key = stack.pop()
                while key != '(':
                    equation.append(key)
                    key = stack.pop()
            else:
                current_weight = get_weight(i)
                stack_weight = get_weight(stack[-1])
                if current_weight > stack_weight:
                    stack.append(i)
                elif current_weight <= stack_weight:
                    while stack and current_weight <= stack_weight:
                        equation.append(stack.pop())
                        if stack:
                            stack_weight = get_weight(stack[-1])
                    stack.append(i)
    while stack:
        equation.append(stack.pop())


    # 수식 계산
    numbers = []
    for i in equation: 
        if i.isdigit():
            numbers.append(i)
        else:
            num1 = int(numbers.pop())
            num2 = int(numbers.pop())
            if i == '*':
                numbers.append(num1 * num2)
            elif i == '+':
                numbers.append(num1 + num2)
    print('#{} {}'.format(tc, *numbers))





        

