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

# 올바른 풀이
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