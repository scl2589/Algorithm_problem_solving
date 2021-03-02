
def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    if answer:
        return sorted(answer)
    else:
        return [-1]

'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (3.57ms, 13.4MB)
테스트 7 〉	통과 (0.28ms, 10.4MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.11ms, 10.3MB)
테스트 10 〉	통과 (0.12ms, 10.3MB)
테스트 11 〉	통과 (0.08ms, 10.3MB)
테스트 12 〉	통과 (0.06ms, 10.2MB)
테스트 13 〉	통과 (0.44ms, 10.4MB)
테스트 14 〉	통과 (0.17ms, 10.3MB)
테스트 15 〉	통과 (0.14ms, 10.3MB)
테스트 16 〉	통과 (0.03ms, 10.2MB)
'''