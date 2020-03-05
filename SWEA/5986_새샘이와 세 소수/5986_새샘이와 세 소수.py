T = int(input())
for tc in range(1, T+1):
    N = int(input())
    primes = []
    #에라토스테네스의 체로 소수를 모두 구한다.
    check = [False, False] + [True] * (N-2)
    for i in range(2, N):
         if check[i]:
             primes.append(i)
             for j in range(2*i, N, i):
                 check[j] = False
    result = 0
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if N - (primes[i] + primes[j]) in primes[j:]:
                result += 1
    print('#{} {}'.format(tc, result))

