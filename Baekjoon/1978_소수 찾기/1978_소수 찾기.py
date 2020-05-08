N = int(input())
nums = list(map(int, input().split()))
count = len(nums)
for i in nums:
    if i == 1:
        count -= 1
        continue
    for j in range(2, i):
        if i % j == 0:
            count  -= 1
            break

print(count)