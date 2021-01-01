M, N = map(int, input().split())
arr = [True] * (N + 1)

for i in range(2, int(N**0.5) + 1):
    if arr[i]:
        for j in range(2*i, N+1, i):
            arr[j] = False

for j in range(M, N+1):
    if j > 1:
        if arr[j] == True:
            print(j)


