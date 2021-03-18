def solution(arr1, arr2):
    answer = []
    for idx, i in enumerate(arr1):
        temp = []
        for j in range(len(arr2[0])):
            num = 0
            for k in range(len(arr2)):
                num += i[k] * arr2[k][j] 
            temp.append(num)
        answer.append(temp)
    return answer

'''
행렬의 곱셈을 할 줄 몰라서 물어봤다 ㅎㅎ 
행렬의 곱셈만 알면 바로 풀 수 있는 문제 :) 
'''
'''
테스트 1 〉	통과 (3.27ms, 10.3MB)
테스트 2 〉	통과 (54.29ms, 11MB)
테스트 3 〉	통과 (56.49ms, 11.4MB)
테스트 4 〉	통과 (3.65ms, 10.3MB)
테스트 5 〉	통과 (38.36ms, 11.1MB)
테스트 6 〉	통과 (21.75ms, 11.1MB)
테스트 7 〉	통과 (3.60ms, 10.3MB)
테스트 8 〉	통과 (0.78ms, 10.2MB)
테스트 9 〉	통과 (0.60ms, 10.4MB)
테스트 10 〉	통과 (38.06ms, 10.6MB)
테스트 11 〉	통과 (6.69ms, 10.2MB)
테스트 12 〉	통과 (1.16ms, 10.4MB)
테스트 13 〉	통과 (28.73ms, 10.8MB)
테스트 14 〉	통과 (57.89ms, 11.2MB)
테스트 15 〉	통과 (18.26ms, 10.6MB)
테스트 16 〉	통과 (6.07ms, 10.7MB)
'''

