from itertools import permutations
N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
arr2 = list(permutations(arr, M))
for i in arr2:
    print(*i)