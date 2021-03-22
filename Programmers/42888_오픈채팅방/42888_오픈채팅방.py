from collections import deque
def solution(record):
    answer = []
    dic = {}
    stack = deque()
    for i in record:
        rec = i.split()
        if rec[0] == "Enter":
            dic[rec[1]] = rec[2]
            stack.append(["enter", rec[1]])
        elif rec[0] == "Leave":
            stack.append(["leave", rec[1]])
        else:
            dic[rec[1]] = rec[2]
    
    for i in stack:
        if i[0] == "enter":
            answer.append(dic[i[1]] + "님이 들어왔습니다.")
        elif i[0] == "leave":
            answer.append(dic[i[1]] + "님이 나갔습니다.")
    return answer

'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.2MB)
테스트 5 〉	통과 (0.94ms, 10.6MB)
테스트 6 〉	통과 (1.05ms, 10.6MB)
테스트 7 〉	통과 (0.80ms, 10.5MB)
테스트 8 〉	통과 (0.93ms, 10.6MB)
테스트 9 〉	통과 (1.08ms, 10.6MB)
테스트 10 〉	통과 (0.98ms, 10.5MB)
테스트 11 〉	통과 (0.54ms, 10.5MB)
테스트 12 〉	통과 (0.52ms, 10.3MB)
테스트 13 〉	통과 (0.96ms, 10.5MB)
테스트 14 〉	통과 (1.06ms, 10.7MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.3MB)
테스트 17 〉	통과 (0.11ms, 10.1MB)
테스트 18 〉	통과 (0.09ms, 10.1MB)
테스트 19 〉	통과 (1.08ms, 10.6MB)
테스트 20 〉	통과 (0.76ms, 10.3MB)
테스트 21 〉	통과 (0.87ms, 10.4MB)
테스트 22 〉	통과 (0.92ms, 10.4MB)
테스트 23 〉	통과 (1.07ms, 10.6MB)
테스트 24 〉	통과 (1.11ms, 10.6MB)
테스트 25 〉	통과 (103.44ms, 49.4MB)
테스트 26 〉	통과 (133.98ms, 53.6MB)
테스트 27 〉	통과 (134.97ms, 57.6MB)
테스트 28 〉	통과 (120.96ms, 59.6MB)
테스트 29 〉	통과 (127.58ms, 59.6MB)
테스트 30 〉	통과 (78.83ms, 49.3MB)
테스트 31 〉	통과 (89.47ms, 58.4MB)
테스트 32 〉	통과 (75.89ms, 53.2MB)
'''


'''
T: 12
'''