# dfs limitation - not working

def dfs(stack):
    if stack:
        num = stack.pop()
        if num == 99:
            return True
        else:
            stack.extend(record[num])
            return dfs(stack)
    else:
        return False
    

for i in range(1, 11):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    record = [list() for _ in range(101)]
    for i in range(0, len(arr), 2):
        record[arr[i]].append(arr[i+1])
    stack = []
    stack.extend(record[0])
    flag = dfs(stack)
    if flag:
        print(f'#{N} 1')
    else:
        print(f'#{N} 0')
