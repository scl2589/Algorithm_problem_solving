from collections import Counter
def solution(nums):
    counted = Counter(nums)
    pick = len(nums) // 2
    if len(counted) > pick:
        return pick 
    else:
        return len(counted) 