for t in range(10):
    N=int(input())
    e=input() # 숫자 한자리
    stack=[]
    back=''
    token={'+':1,'*':2,'(':0}
    for ch in e:
        if ch==')':
            while stack[-1]!='(':
                back+=stack.pop()
            stack.pop()
        elif ch=='(':
            stack.append(ch)
        elif  ch=='+' or ch=='*':
            while stack: 
                if token[ch]<token[stack[-1]]:
                    back+=stack.pop()
                else:
                    break
            stack.append(ch)
        else:
            back+=ch
    while stack:
        back+=stack.pop()
     
    for ch in back:
        if ch=='+':
            stack.append(stack.pop()+stack.pop())
        elif ch=='*':
            stack.append(stack.pop()*stack.pop())
        else:
            stack.append(int(ch))
    print('#{} {}'.format(t+1,stack.pop()))