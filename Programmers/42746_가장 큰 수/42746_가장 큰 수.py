def solution(numbers):
    arr = list(map(str, numbers))
    arr.sort(key = lambda x: (x[0], x[1%len(x)], x[2%len(x)], x[3%len(x)]), reverse = True)
    answer = ''.join(arr)
    if int(answer) != 0:
        return answer
    else:
        return "0"

'''
테스트 1 〉	통과 (282.23ms, 24.3MB)
테스트 2 〉	통과 (101.54ms, 17.8MB)
테스트 3 〉	통과 (458.46ms, 28.6MB)
테스트 4 〉	통과 (2.59ms, 10.5MB)
테스트 5 〉	통과 (230.70ms, 22.8MB)
테스트 6 〉	통과 (182.67ms, 21.2MB)
테스트 7 〉	통과 (0.05ms, 10.4MB)
테스트 8 〉	통과 (0.04ms, 10.3MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉 통과 (0.03ms, 10.2MB)
테스트 11 〉 통과 (0.06ms, 10.3MB)
'''
'''
T: 1시간
다시 풀어봐야 할 문제!! 
permutations를 사용하면 시간 초과가 나고 (numbers 길이가 최대 10만이므로)
'30' 및  '34'와 같은 숫자를 처리해주는 부분이 어려웠다. 
다른 블로그 참고하여 풀었다.
'''

# 시간 초과 코드 
# from itertools import permutations
# def solution(numbers):
#     comb = list(permutations(numbers, len(numbers)))
#     arr = sorted([''.join(list(map(str, each))) for each in comb])
#     return arr[-1]