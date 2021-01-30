# 시간초과 코드 
# N = int(input())
# distances = list(map(int, input().split()))
# costs = list(map(int, input().split()))
# total = 0

# def find_min(original):
#     for i in range(original, N):
#         if costs[original] > costs[i]:
#             return i
#     else:
#         return 0

# i = 0
# while i < len(costs):
#     if min(costs) == costs[i]:
#         total += sum(distances[i:]) * costs[i]
#         break
#     elif costs[i] != max(costs):
#         small = find_min(i)
#         total += sum(distances[i:small]) * costs[i]
#         i = small
#     else:
#         total += distances[i] * costs[i]
#         i += 1

# print(total)


# 두번쨰 코드 
N = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))[:N-1]
total = 0

min_num = float('inf')
for i in range(N-1):
    min_num = min(min_num, costs[i])
    total += min_num * distances[i]
print(total)