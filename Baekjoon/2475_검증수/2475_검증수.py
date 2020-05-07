nums = list(map(str, input().split()))
total = 0
for i in nums:
    total += int(i) ** 2
print(total % 10)