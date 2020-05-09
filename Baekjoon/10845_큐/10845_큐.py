# 시간초과 코드
N = int(input())
result = []
for i in range(N):
    cmd = list(input().split())
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
        if len(result) != 0:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if len(result)!= 0:
            print(result[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(result)!= 0:
            print(result[-1])
        else:
            print(-1)
    