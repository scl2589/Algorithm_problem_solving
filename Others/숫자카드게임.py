N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0

for i in range(N):
    # 해당 행의 minimum 값을 저장한다.
    temp_min = min(arr[i])

    # 이전 최소값과 현재 행의 최소값을 비교해 최대값을 구한다.
    result = max(result, temp_min)

print(result)