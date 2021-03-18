class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort() 
        return sum([i for i in nums[::2]])

'''
Runtime: 264 ms, faster than 69.51% of Python3 online submissions for Array Partition I.
Memory Usage: 16.9 MB, less than 61.93% of Python3 online submissions for Array Partition I.
'''

