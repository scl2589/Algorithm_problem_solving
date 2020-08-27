n, k = map(int, input().split())
answer = 0

while n >= k:
    # n이 k로 한 번에 딱 나누어 떨어지는 수가 될 때 까지 1을 빼기
    target = (n // k) * k 

    # 한 번에 안떨어진다면 빼야 하는 횟수! 
    answer += (n - target)
    n = target

    # K로 나누기
    answer += 1
    n //= k

answer += (n-1)
print(answer)