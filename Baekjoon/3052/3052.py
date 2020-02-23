nums = []
for i in range(10):
    nums.append(int(input()))

remainder = []
for i in nums:
    if (i % 42) in remainder:
        continue
    else:
        remainder.append(i % 42)


print(len(remainder))