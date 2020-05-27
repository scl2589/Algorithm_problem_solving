# 이분탐색을 이용한다.
import sys
K, N = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(arr)
while start <= end:
    mid = (start + end) //2 # 중간 위치를 구한다.
    num_lan = 0 #랜선 수 
    for i in arr:
        num_lan += i // mid
    if num_lan >= N: # 랜선의 개수가 N과 같거나 크다면
        start = mid + 1
    else:
        end = mid - 1
print(end)


""" 시간초과: 실패코드 
import sys
K, N = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(K)]
median = sum(arr) // N
while True:
    count = 0
    for i in arr:
        count += i//median
    if count == N:
        print(median)
        break
    else:
        median -= 1 
"""
