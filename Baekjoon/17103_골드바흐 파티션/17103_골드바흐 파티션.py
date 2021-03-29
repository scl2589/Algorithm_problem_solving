T = int(input())
nums = [int(input()) for _ in range(T)]
m = max(nums)

# 소수 구하기 - 에라토스테네스의 체 
primes = [False, False] + [True] * (m - 1)
for i in range(2, int(m**0.5)+1):
    if primes[i]:
        for j in range(2 * i, m + 1, i):
            primes[j] = False

# 두 수가 모두 소수인 경우 찾기
for num in nums:
    count = 0
    for i in range((num//2)+1):
        if primes[i] and primes[num-i]:
            count += 1
    print(count)