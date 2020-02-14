def solution(heights):
    answer = []
    
    for i in range(len(heights)):
        stack = []
        for j in range(i):
            if heights[i] < heights[j]:
                stack.append(j+1)
        if len(stack)!= 0:
            answer.append(stack.pop())
        else:
            answer.append(0)

    return(answer)