def solution(heights):
    answer = []
    for i in range(len(heights)):
        for j in range(i, -1, -1):
            if heights[i] < heights[j]:
                answer.append(j+1)
                break
        else:
            answer.append(0)

    return(answer)