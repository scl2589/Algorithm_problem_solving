N = int(input())
nums = list(map(int, input().split()))
count = 1
maxV = 1
for i in range(1, N):
    if nums[i-1] >= nums[i]:
        count += 1
    else:
        count = 1
    maxV = max(count, maxV)
count = 1
for j in range(1, N):
    if nums[j-1] <= nums[j]:
        count += 1
    else:
        count = 1
    maxV = max(count, maxV)
print(maxV)