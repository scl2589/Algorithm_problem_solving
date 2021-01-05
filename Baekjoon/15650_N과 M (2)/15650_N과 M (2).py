N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
check = [False] * N 
arr = []

def backtracking(depth):
    if depth == M:
        print(*arr)
        return 
    for i in range(0, N):
        if check[i]:
            continue 
        check[i] = True 
        arr.append(numbers[i])
        backtracking(depth + 1)
        arr.pop() 
        for j in range(i + 1, N):
            check[j] = False 

backtracking(0)
