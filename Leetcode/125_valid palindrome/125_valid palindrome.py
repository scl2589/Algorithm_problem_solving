class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 대소문자는 구분하지 않고, 영문자와 숫자만을 대상으로 함
        sentence = ""
        for i in s:
            if i.isalnum():
                sentence += i.lower()
        if sentence == sentence[::-1]:
            return True
        else:
            return False

# 데크 자료형을 이용한 최적화
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 대소문자는 구분하지 않고, 영문자와 숫자만을 대상으로 함
        deq = collections.deque()
        for char in s:
            if char.isalnum():
                deq.append(char.lower())
        while len(deq)>1:
            if deq.popleft() != deq.pop():
                return False
        return True

# 슬라이싱 및 정규식 사용 (36ms로 가장 빠름)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 대소문자는 구분하지 않고, 영문자와 숫자만을 대상으로 함
        s = s.lower()
        # 정규식으로 불필요한 문자를 필터링한다.
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]