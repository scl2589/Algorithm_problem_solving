# 44ms
# in 을 이용해 탐색 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            difference = target - num
            if difference in nums[idx+1:]:
                return [idx, nums[idx+1:].index(difference) + (idx + 1)]

# 40 ms
# dictionary를 이용한 첫 번째 수를 뺸 결과 key 조회
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = dict()
        #키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        # 타겟에서 첫 번째 수를 뺸 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return nums.index(num), nums_map[target-num]

# 48ms
# 조회 구조 개선
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        
        #하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i