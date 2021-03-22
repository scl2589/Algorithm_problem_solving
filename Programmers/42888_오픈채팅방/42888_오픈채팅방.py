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