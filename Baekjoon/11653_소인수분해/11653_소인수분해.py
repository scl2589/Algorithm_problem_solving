N = int(input())
while True:
    for i in range(2, N):
        if N % i == 0:
            print(i)
            N //= i
            break 
    else:
        print(N)
        break