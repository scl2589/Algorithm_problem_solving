# 여행에 필요하다고 생각하는 N개의 물건
# 각 물건은 무게 w와 가치 V를 가지는데
# 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다.
# 준서는 각 최대 K만큼 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
# 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최대값을 알려주자.


# 시간초과 나는 코드 (dfs로는 풀이 불가!!)
N, K = map(int, input().split())
arr = []
for _ in range(N):
    w, v = map(int, input().split())
    arr.append([w, v])

val = 0
def sol(depth, tot_weight, tot_val):
    global val 
    if depth == N:
        if tot_weight <= K:
            val = max(val, tot_val)
        return 
    if tot_weight > K:
        return
    else:
        val = max(val, tot_val)
        sol(depth + 1, tot_weight + arr[depth][0], tot_val + arr[depth][1])
        sol(depth + 1, tot_weight, tot_val)

sol(0, 0, 0)

print(val)

#dp를 이용해야한다.
# 1) 만약 넣고자 하는 물건의 크기가 해당 dp의 크기보다 크다면 dp[i-1][w]로 바로 이전값을 가져와서 저장한다.
# 2) 만약 해당 w에 해당 물건을 넣을 수 있다면 이제 이전 물건까지 넣었던 값 중 최대값을 비교 해주어야 한다.
'''
예시) 
물건 1, 2, 3, 4, 5가 있으면 현재 3을 넣고 싶을때이면 1과 2는 넣어본 상태이다.
3번이 들어갈 정도의 w가 남아있다면, dp[i-1][w-w3] 이렇게 이전의 row에 3번이 들어갈 공간을 비워둔 곳에 value에 3번의 value를 저장한다.
위의 값과 그냥 dp[i-1][w]를 비교해서 큰 값을 dp[i][w]에 저장한다. 
'''
import sys 
r = sys.stdin.readline
N, W = map(int, r().split())
bag = [tuple(map(int, r().split())) for _ in range(N)]

knap = [0 for _ in range(W+1)]

for i in range(N):
    for j in range(W, 1, -1):
        if bag[i][0] <= j:
            knap[j] = max(knap[j], knap[j-bag[i][0]] + bag[i][1])

print(knap[-1])