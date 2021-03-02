# 에라토스테네스의 체 
def solution(n):
    answer = 0
    visit = [True] * (n+1)
    
    m = int(n**0.5)
    for i in range(2, m+1):
        if visit[i] == True:
            for j in range(i*i, n+1, i):
                visit[j] = False 
    arr = [i for i in range(2, n+1) if visit[i] == True]
    return len(arr)

'''
정확성 테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.09ms, 10.3MB)
테스트 4 〉	통과 (0.17ms, 10.2MB)
테스트 5 〉	통과 (0.12ms, 10.3MB)
테스트 6 〉	통과 (1.46ms, 10.4MB)
테스트 7 〉	통과 (0.44ms, 10.3MB)
테스트 8 〉	통과 (1.18ms, 10.3MB)
테스트 9 〉	통과 (1.70ms, 10.3MB)
테스트 10 〉	통과 (37.96ms, 13MB)
테스트 11 〉	통과 (122.34ms, 19.5MB)
테스트 12 〉	통과 (42.02ms, 13.7MB)
효율성  테스트
테스트 1 〉	통과 (132.46ms, 20.1MB)
테스트 2 〉	통과 (125.13ms, 19.9MB)
테스트 3 〉	통과 (129.50ms, 20.1MB)
테스트 4 〉	통과 (126.38ms, 19.9MB)
'''