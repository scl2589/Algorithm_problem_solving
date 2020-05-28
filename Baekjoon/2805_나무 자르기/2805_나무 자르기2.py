#import sys
#sys.stdin = open('input.txt')
N, M = map(int, input().split())
heights = list(map(int, input().split()))

start = 0
end = max(heights)

while start <= end:
    mid = (start + end) // 2
    height_total = 0
    for i in heights:
        if i >= mid:
            height_total += i - mid
    if height_total >= M:
        start = mid + 1
    else:
        end = mid -1

print(end)
