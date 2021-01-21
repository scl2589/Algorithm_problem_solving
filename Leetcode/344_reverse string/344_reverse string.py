class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # s.reverse()
        s[:] = s[::-1]
        # s[:] 이러한 방식으로 사용해야 되는 이유는
        # 공간 복잡도를 O(1)로 제한하다보니 변수 할당을 처리하는데 다소 제약이 있기 때문이다.

# 투 포인터를 이용한 방식 
# 하지만 reverse 방식 (위 방식) 이 더 빠르다.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1