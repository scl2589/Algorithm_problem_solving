# 시간초과
"""
N = int(input())
nums = [i for i in range(1, N+1)]
while len(nums) != 1:
    del nums[0]
    took_out = nums.pop(0)
    nums.append(took_out)
print(*nums)
"""
#collections.deque 라이브러리를 이용해 시간을 축소했습니다.
from collections import deque
nums = deque([i for i in range(1, int(input())+1)])
while len(nums) != 1:
    nums.popleft()
    nums.rotate(-1)
print(*nums)