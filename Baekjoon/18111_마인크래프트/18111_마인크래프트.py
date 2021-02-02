# 시간초과
'''
세로 N, 가로 M 크기의 집터 
집터 맨 왼쪽 위 좌표 (0, 0)
목적: 이 집터 내의 당 높이를 일정하게 바꾸는 것.
- 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. - 2초
- 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다. - 1초

땅 고르기에 걸리는 최소 시간과 땅의 높이 

# 단 집터 아래에 동굴 등 빈 공간은 존재하지 않으며, 집터 바깥에서 블록을 가져올 수 없다.
작업을 시작할 때 인벤토리에 b개 블록 존재.
땅의 높이는 256 블록 초과를 못하고, 음수가 될 수 없다.
'''
N, M, B = map(int, input().split())
land = []
for _ in range(N):
    land.extend(map(int, input().split()))
max_land = max(land)
min_land = min(land)

if max_land > 256:
    max_land = 255
count = float('inf')
answer = 0

for h in range(min_land, max_land + 1):
    storage = B
    temp = 0
    fail = False
    for block in land:
        # 만약 기준보다 블록의 높이가 더 작으면 
        if block < h:
            # 저장고에서 블록을 빼와 그만큼 쌓아준다.
            storage -= (h - block)
            # 저장고가 0 보다 작으면 이 판은 끝낼 것.
            if storage < 0:
                fail = True 
                break 
            # 블록 옮기는데 얼마나 소요되는지 계산하기 
            temp += h-block
        # 만약 기준치보다 블록의 높이가 더 높다면? 
        elif block > h:
            # 블록을 그만큼 빼서 저장고에 추가한다.
            storage += block - h 
            temp += (block-h)*2
            
    # 실패하지 않았다면
    if not fail: 
        if count > temp:
            count = temp 
            answer = h 

print(count, answer)

# 시간초과 2
import sys
N, M, B = map(int, sys.stdin.readline().split())
land = []
for _ in range(N):
    land.extend(map(int, input().split()))

height = 0
ans = 1000000000000000000000000000000

for i in range(256):
    max_land = 0
    min_land = 0
    for block in land: 
        # 현재 블록이 기준보다 작다면 인벤토리에서 제외하여 블록 위에 몇개를 놓아야 하는지 센다.
        if block < i: 
            min_land += (i-block)
        # 현재 블록이 기준보다 크다면 인벤토리에 몇개를 넣어야 하는지 센다.
        else:
            max_land += (block - i)
    # 저장소에 있는 개수는 인벤토리의 수 + 인벤토리에 넣은 개수를 합한 값이다.
    inventory = max_land + B
    # 만약 인벤토리에서 제외한 값이 저장소에 있는 값보다 크다면.. 컨티뉴
    if inventory < min_land:
        continue
    #시간을 계산한다 
    time = 2 * max_land + min_land
    if time <= ans:
    # 시간이 같을 때는 높이가 높은 순으로 출력하라는 조건에 맞게
    # for i in range(257)은 항상 i가 오름차순으로 돌기 때문에
    # 시간이 같아도 최종적으로는 높이가 높은 순으로 나오게 된다
        ans = time
        height = i
print(ans, height)


#진짜 답안 
from collections import Counter


def make_land(height):
	sec = 0
	for key in land:
		if key < height:
			sec += (height - key) * land[key]
		elif key > height:
			sec += (key - height) * 2 * land[key]
	return sec


n, m, inven = map(int, input().split())
land = []
for _ in range(n):
	land += map(int, input().split())

_sum, _len = sum(land), n * m
land = dict(Counter(land))
height, min_sec = 0, 100000000000000

for i in range(257):

	if _len * i <= _sum + inven:
		sec = make_land(i)
		if sec <= min_sec:
			min_sec = sec
			height = i

print(min_sec, height)