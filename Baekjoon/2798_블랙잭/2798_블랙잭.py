N, M = map(int, input().split())
nums = list(map(int, input().split()))
diff = []
summation = []
for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            total = nums[i] + nums[j] + nums[k]
            if total <= M:
                diff.append(M-total)
                summation.append(total)
min_idx = diff.index(min(diff))
print(summation[min_idx])