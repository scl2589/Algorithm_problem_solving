from collections import deque
def solution(heights):
    stack = deque()
    answer = []
    for idx, value in enumerate(heights):
        if idx == 0:
            stack.append([idx+1, value])
            answer.append(0)
        else:
            count = 0
            for i in range(len(stack)-1, -1, -1):
                if stack[i][1] > value:
                    answer.append(stack[i][0])
                    break
                else:
                    count += 1
            if count == idx:
                answer.append(0)
            stack.append([idx+1,value])
    return answer


#뒤에서부터 기둥의 높이와 위치를 스택에다가 쌓기
#스택에 쌓기 전, 스택에 자기보다 낮은 높이의 기둥이 있다면 해당되는 기둥들을 모두 pop하고, 스택에서 pop한 기둥의 answer값을 현재 기둥의 값으로 하면 됩니다.