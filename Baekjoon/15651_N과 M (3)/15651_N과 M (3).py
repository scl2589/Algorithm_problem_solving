# 방법 1 (1968ms)
N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
arr = []

def backtrack(depth):
    if depth == M:
        print(*arr)
        return 
    for i in range(N):
        arr.append(numbers[i])
        backtrack(depth + 1)
        arr.pop() 

backtrack(0)

# 방법 2 (짧은 시간 - 500ms)
from itertools import product

n,m = list(map(int, input().split()))

li = list(map(str, range(1,n+1)))
per = product(li, repeat=m)

print('\n'.join(list(map(' '.join, sorted(per)))))

#방법 3 (더 짧은 시간 - 244ms)
from itertools import product as pd

N,M = map(int, input().split())
a = map(str, range(1,N+1))
print('\n'.join(list(map(' '.join,pd(a,repeat=M)))))