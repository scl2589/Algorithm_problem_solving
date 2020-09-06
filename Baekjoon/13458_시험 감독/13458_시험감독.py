import math

N = int(input())
students = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0

for i in students:
    ans += 1
    remain = i - B 
    if i - B > 0:
        ans += math.ceil(remain/C)

print(ans)