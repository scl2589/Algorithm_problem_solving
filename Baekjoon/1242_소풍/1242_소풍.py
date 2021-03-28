N, K, M = map(int,input().split())
original_N = N
while True:
    mod = K % N
    if mod == 0:
        mod = N
    if mod == M:
        break
    elif mod < M:
        M = M - mod
    else:
        M = M - mod + N
    N -= 1
print(original_N - N + 1)