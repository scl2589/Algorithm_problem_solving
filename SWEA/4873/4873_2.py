T = int(input())

for tc in range(1, T+1):
    stack = []
    D = input()
    for c in D:
        if len(stack) != 0:
            if stack[-1] ==c:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)

    print('#{} {}'.format(tc,len(stack) ))
