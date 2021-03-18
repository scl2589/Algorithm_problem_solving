import math 
def solution(brown, yellow):
    answer = []
    total = brown + yellow 
    candidates = []
    for i in range(3, math.ceil(total**0.5)+1):
        if total % i == 0:
            candidates.append([i, total // i])
    if len(candidates) == 1:
        answer = candidates[0]
    else:
        for candidate in candidates:
            if (candidate[0] - 2) * (candidate[1] - 2) == yellow:
                answer = candidate
                break
    # 가로 길이는 세로 길이보다 길다 
    if answer[0] < answer[1]:
        answer[0], answer[1] = answer[1], answer[0]
    return answer
'''
T: 15
1. 먼저 나눠 떨어지는 숫자 구하기 (brown + yellow 숫자 기반)
2. 그 숫자 후보들 중에서 1과 2로 나누어진다면 제외 
3. 나머지 후보에서 가로에서 2를 빼고, 세로에서 2를 뻈을 때 yellow 숫자라면 패스 
'''

'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.10ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.08ms, 10.2MB)
테스트 7 〉	통과 (0.13ms, 10.3MB)
테스트 8 〉	통과 (0.11ms, 10.3MB)
테스트 9 〉	통과 (0.12ms, 10.3MB)
테스트 10 〉	통과 (0.12ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
'''

# 더 짧은 코드 작성!
import math 
def solution(brown, yellow):
    answer = []
    total = brown + yellow 
    for i in range(3, math.ceil(total**0.5)+1):
        if total % i == 0:
            a, b = i, total//i
            if (a - 2) * (b - 2) == yellow:
                if b > a:
                    a, b = b, a
                return [a, b]