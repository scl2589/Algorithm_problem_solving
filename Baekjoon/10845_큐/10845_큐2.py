# stdin.readline()을 사용하면 시간이 훨씬 더 빠르다.
from sys import stdin
result = []
for i in range(int(stdin.readline())):
    cmd = list(stdin.readline().split())
    if cmd[0] == 'push':
        result.append(cmd[1])
    elif cmd[0]=='pop':
        if result:
            print(result.pop(0))
        else:
            print(-1)
    elif cmd[0]=='size':
        print(len(result))
    elif cmd[0]=='empty':
        if result:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if result:
            print(result[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if result:
            print(result[-1])
        else:
            print(-1)
    

    