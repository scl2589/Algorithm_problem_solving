T = int(input())
def find_prime(N):
    for i in range(2, N):
        if N % i == 0:
            return False 
    return True

for _ in range(T):
    N = int(input())
    a = N // 2
    b = N - a


    while True: 
        if find_prime(a):
            if find_prime(b):
                print(a, b)
                break 
        a -= 1
        b += 1