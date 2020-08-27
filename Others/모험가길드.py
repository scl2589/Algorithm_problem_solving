N = int(input())
arr = list(map(int, input().split()))

arr.sort()
total = 0
count = 0

for i in arr:
    total += 1
    if total >= i:
        count +=1
        total = 0

print(count)