#import sys
#sys.stdin = open('input.txt')
# Python3로 제출하면 시간 초과 코드, Pypy3로는 맞는 코드
N, M = map(int, input().split())
heights = list(map(int, input().split()))

start = 0
end = max(heights)
minV = float('inf')
ans = 0

while True:
    if start > end:
        flag = True
        break
    mid = (start + end) // 2
    height_total = 0
    for i in heights:
        cut = i - mid
        if cut <= 0:
            continue
        else:
            height_total += cut
    if height_total == M:
        ans = mid
        break
    elif height_total > M:
        if minV > height_total - M:
            minV = height_total - M
            ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)
