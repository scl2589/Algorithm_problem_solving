while True:
    N = int(input())
    if N == 0:
        break
    arr = [True] * (2 * N + 1)
    for i in range(2, int((2*N)**0.5) + 1):
        if arr[i]:
            for j in range(2*i, 2*N + 1, i):
                arr[j] = False 
    count = 0
    for j in range(N + 1, 2*N + 1):
        if j > 1:
            if arr[j] == True:
                count += 1
    print(count)