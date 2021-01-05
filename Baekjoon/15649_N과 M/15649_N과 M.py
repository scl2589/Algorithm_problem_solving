# 방법 1

# from itertools import permutations
# N, M = map(int, input().split())
# arr = [i for i in range(1, N + 1)]
# arr2 = list(permutations(arr, M))
# for i in arr2:
#     print(*i)


# 방법 2
N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
visited = [False] * N 

def backtracking(n, k, ans):
    global visited
    if n == k:
        print(ans)
        return 
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            backtracking(n+1, k, ans.append(arr[i]))
            visited[i] = False 
            backtracking(n, k, ans)


backtracking(0, M, [])