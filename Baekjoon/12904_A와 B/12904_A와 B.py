S = list(map(str, input()))
T = list(map(str, input()))

flag = False

while T:
    if S == T:
        flag = True 
        break
    if T[-1] == 'B':
        T.pop() 
        T = T[::-1]
    elif T[-1] == 'A':
        T.pop()
    
if flag:
    print(1)
else:
    print(0)