N, M = map(int, input().split())
arr = list(map(int, input().split()))

array = [0] * 11

for x in arr:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0

# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, M+1):
    n -= array[i] #무게가 i인 볼링공의 개수 (A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)