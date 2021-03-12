def solution(name):
    answer = 0
    idx = 0
    word = [i for i in name]
    
    while True: 
        if word[idx] != 'A':
            answer += min(ord(name[idx])- ord('A'), (ord('Z') - ord(name[idx])+1))
        word[idx] = 'A'
        if set(word) == {'A'}:
            break
        left, right = 1, 1
        while word[idx+right] == 'A':
            right += 1
        while word[idx-left] == 'A':
            left += 1
        
        if right <= left:
            answer += right
            idx += right 
        else:
            answer += left
            idx -= left
    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)

'''

'''
T: 1시간 반.. 다시 풀어보자 
막상 풀고나니 생각보다 코드 구현은 간단했다. 
왼쪽과 오른쪽으로 향했을 때 A를 안만나기까지 더 적은횟수를 카운팅한다.
'''

# 시간초과 코드
# def movePrev(name, idx):
#     if idx == 0:
#         idx = len(name) - 1
#     else:
#         idx -= 1
#     return idx 

# def moveNext(name, idx):
#     if idx == len(name) - 1: 
#         idx = 0
#     else:
#         idx += 1
#     return idx


# def solution(name):
#     answer = 0
#     idx = 0
#     word = ['A' for i in range(len(name))]
#     check = [False] * (len(name))
#     alphabets = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    
#     while True: 
#         if name[idx] != 'A':
#             count = min(ord(name[idx])- ord('A'), (ord('Z') - ord(name[idx])+1))
#             answer += count
#             word[idx] = name[idx]
#             check[idx] = True
#             if ''.join(word) == name:
#                 break
#         else:
#             answer += 1
#             check[idx] = True
#         if name[movePrev(name, idx)] == 'A':
#             idx = moveNext(name, idx)
#             answer += 1
#         else:
#             idx = movePrev(name, idx)
#             answer += 1
#     return answer