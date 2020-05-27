import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

# 1. 산술평균
print(round(sum(nums)/N))

# 2. 중앙값
nums.sort()
print(nums[N//2])

# 3. 최빈값 (여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.)
# Counter를 활용한다.
diction = Counter(nums).most_common()
if len(nums) > 1:
    if diction[0][1] == diction[1][1]:
        print(diction[1][0])
    else:
        print(diction[0][0])
else:
    print(diction[0][0])


# 4. 범위
print(max(nums) - min(nums))