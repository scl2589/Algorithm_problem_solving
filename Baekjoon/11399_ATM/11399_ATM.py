N = int(input())
P = sorted(list(map(int, input().split())))

total = 0
for i in range(N):
    total += sum(P[:i+1])

print(total)