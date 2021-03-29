from itertools import combinations_with_replacement

nums = [1, 5, 10, 50]
N = int(input())

arr = set()

for combi in combinations_with_replacement(range(4), N):
    temp_sum = 0
    for i in combi:
        temp_sum += nums[i] 
    if temp_sum not in arr:
        arr.add(temp_sum)
print(len(arr))