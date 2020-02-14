from collections import deque
def solution(prices):
    stack = deque(prices)
    answer = []
    for i in range(len(prices)):
        count = 0
        a = stack.popleft()
        for j in range(i+1, len(prices)):
            if a <= prices[j]:
                count += 1
            else:
                count +=1
                break
        answer.append(count)
                

    return answer
