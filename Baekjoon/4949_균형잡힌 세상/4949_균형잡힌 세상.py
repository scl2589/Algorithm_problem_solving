import sys
while True:
    flag = False
    sentence = list(sys.stdin.readline().strip('\n'))
    if sentence[0] == '.' and len(sentence) == 1:
        break
    else:
        stack = []
        for i in sentence:
            if i in ('[', ']', '(', ')'):
                if stack:
                    if i == '[' or i=='(':
                        stack.append(i)
                    else:
                        if stack[-1] == '(' and i == ')':
                            stack.pop()
                        elif stack[-1] == '[' and i == ']':
                            stack.pop()
                        else:
                            print('no')
                            flag = True
                            break
                else:
                    if i == '[' or i == '(':
                        stack.append(i)
                    elif i == ']' or i == ')':
                        print('no')
                        flag = True
                        break
        if flag:
            continue
        if stack:
            print("no")
        else:
            print("yes")