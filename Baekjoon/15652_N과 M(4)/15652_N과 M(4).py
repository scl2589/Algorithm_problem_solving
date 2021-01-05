N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
check = [False] * N
arr = []

def backtrack(depth):
    if depth == M:
        print(*arr)
        return 
    for i in range(N):
        if check[i]:
            continue
        arr.append(numbers[i])
        backtrack(depth + 1)
        check[i] = True
        arr.pop() 

        for i in range(i+1, N):
            check[i] = False 

backtrack(0)