
def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
                
    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.08ms, 10.2MB)
테스트 3 〉	통과 (1.12ms, 10.3MB)
테스트 4 〉	통과 (1.09ms, 10.4MB)
테스트 5 〉	통과 (1.32ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.1MB)
테스트 7 〉	통과 (0.71ms, 10.2MB)
테스트 8 〉	통과 (0.88ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.1MB)
테스트 10 〉	통과 (1.34ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (125.03ms, 18.7MB)
테스트 2 〉	통과 (98.33ms, 17.6MB)
테스트 3 〉	통과 (155.24ms, 19.5MB)
테스트 4 〉	통과 (111.12ms, 18.3MB)
테스트 5 〉	통과 (74.95ms, 17MB)
'''