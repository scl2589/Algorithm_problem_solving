N = int(input())
if N == 1:
    pass
else:
    while True:
        for i in range(2, N):
            if N % i == 0:
                print(i)
                N //= i
                break 
        else:
            print(N)
            break