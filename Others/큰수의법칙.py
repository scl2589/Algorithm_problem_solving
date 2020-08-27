# 문제 및 해설은 scl2589.github.io 블로그를 참고해주시기 바랍니다.
N, M, K = map(int, input().split())

arr = list(map(int, input().split()))

# 정렬하기
arr.sort()

# 가장 큰 수
largest = arr[-1]

# 두 번째로 큰 수
second = arr[-2]

result = 0
# 가장 큰 수가 더해지는 횟수 계산 
result += M // K * K * largest
# 두번째로 큰 수 더하기 
result += M % K * second

print(result)
