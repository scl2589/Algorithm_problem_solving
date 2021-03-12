
def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)
                
    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.08ms, 10.2MB)
테스트 3 〉	통과 (1.11ms, 10.3MB)
테스트 4 〉	통과 (1.12ms, 10.4MB)
테스트 5 〉	통과 (1.24ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.64ms, 10.2MB)
테스트 8 〉	통과 (0.87ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.1MB)
테스트 10 〉	통과 (1.29ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (123.34ms, 18.9MB)
테스트 2 〉	통과 (95.35ms, 17.6MB)
테스트 3 〉	통과 (152.07ms, 19.5MB)
테스트 4 〉	통과 (109.73ms, 18.3MB)
테스트 5 〉	통과 (73.53ms, 17.1MB)
'''