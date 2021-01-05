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
s = []

def backtracking():
    if len(s) == M:
        print(*s)
        return 
    for i in range(1, N+1):
        if i in s:
            continue 
        s.append(i)
        backtracking()
        s.pop() 


backtracking()