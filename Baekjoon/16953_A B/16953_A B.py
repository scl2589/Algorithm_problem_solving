A, B = map(int, input().split())
ans = float('inf')

def dfs(total, count):
    global ans
    if total > B:
        return
    if total == B:
        ans = min(ans, count)
        return

    count += 1
    dfs(total*2, count)
    dfs(int(str(total)+'1'), count)

dfs(A, 1)
if ans != float('inf'):
    print(ans)
else:
    print(-1)