#for문과 combinations
from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chicken=[]
house=[]
total_dist = float('inf')

for i in range(N):
    for j in range(len(arr[0])):
        if arr[i][j]==2:
            chicken.append([i, j])
        elif arr[i][j] == 1:
            house.append([i, j])

for each_chicken in combinations(chicken, M):
    dist = 0
    for house_pos in house:
        min_dist = float('inf')
        for chicken_pos in each_chicken:
            temp_dist = abs(house_pos[0]-chicken_pos[0]) + abs(house_pos[1]-chicken_pos[1])
            if temp_dist < min_dist:
                min_dist = temp_dist
        dist += min_dist
    if dist < total_dist:
        total_dist = dist
print(total_dist)
