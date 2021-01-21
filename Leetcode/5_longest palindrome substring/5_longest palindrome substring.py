# 시간 초과 코드 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        else:
            answers = list(s)
            for i in range(1, len(s) + 1):
                for j in range(len(s) - i + 1 ):
                    if j == 0:
                        if s[j:j+i] == s[j+i-1::-1]:
                            answers.append(s[j:j+i])
                    else:
                        if s[j:j+i] == s[j+i-1:j-1:-1]:
                            answers.append(s[j:j+i])
            answers.sort(key = lambda x : len(x), reverse=True)
            return answers[0]

# 올바른 풀이 (이 방식이 하단의 투 포인터 풀이보다 빠르다)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        i,l=0,0
        for j in range(len(s)):
            if s[j-l: j+1] == s[j-l: j+1][::-1]:
                i, l = j-l, l+1
                # print(s[i: i+l])
            elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
                i, l = j-l-1, l+2
                # print(s[i: i+l])
        return s[i: i+l]

# 투포인터 방식으로 풀이
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left+1:right-1]
    
        # 해당 사항이 없을 경우엔 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s
    
        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s)-1):
            result = max(result,
                        expand(i, i+1), 
                        expand(i, i+2),
                        key = len)
        return result