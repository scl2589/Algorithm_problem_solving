# 시간초과 코드
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            product = 1
            # 왼쪽 곱셈 
            if i >= 1:
                for j in nums[:i]:
                    product *= j
            # 오른쪽 곱셈
            if i < len(nums) - 1:
                for j in nums[i+1:]:
                    product *= j
            answer.append(product)
        return answer

# 왼쪽 곱셈값에 오른쪽 값을 차례대로 곱셈 하는 방법
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        p = 1
        for i in range(len(nums)):
            # 왼쪽 곱셈 
            answer.append(p) 
            p *= nums[i]

        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈:
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= p 
            p *= nums[i]
        return answer