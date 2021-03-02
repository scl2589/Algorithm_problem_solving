def solution(s, n):
    loweralpha = "abcdefghijklmnopqrstuvwxyz"
    upperalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for i in s:
        if i == ' ':
            answer += i 
        else:
            # 대문자
            if ord(i) <= 96: 
                idx = upperalpha.index(i)
                calc = (idx + n ) % 26
                answer += upperalpha[calc]
            else:
                idx = loweralpha.index(i)
                calc = (idx + n) % 26
                answer += loweralpha[calc]
    return answer

'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.4MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (3.26ms, 10.2MB)
'''

# 다른 사람 풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
    # 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))