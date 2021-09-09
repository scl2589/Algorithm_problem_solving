def solution(numbers, hand):
    dict = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8:[2, 1], 9: [2,2], '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    left = [3, 0]
    right = [3, 2]
    answer = ''
    for num in numbers:
        if num in [1, 4, 7]:
            left = dict[num]
            answer += 'L'
        elif num in [3, 6, 9]:
            right = dict[num]
            answer += 'R'
        else:
            pos = dict[num]
            left_dist = abs(left[0]-pos[0]) + abs(left[1]-pos[1])
            right_dist = abs(right[0]-pos[0]) + abs(right[1]-pos[1])
            if left_dist < right_dist:
                left = pos
                answer += 'L'
            elif right_dist < left_dist:
                right = pos
                answer += 'R'
            else:
                if hand == "right":
                    right = pos 
                    answer += 'R'
                else:
                    left = pos
                    answer += 'L'
        
    return answer


'''
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.4MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.3MB)
테스트 14 〉	통과 (0.06ms, 10.3MB)
테스트 15 〉	통과 (0.16ms, 10.3MB)
테스트 16 〉	통과 (0.15ms, 10.4MB)
테스트 17 〉	통과 (0.33ms, 10.2MB)
테스트 18 〉	통과 (0.29ms, 10.3MB)
테스트 19 〉	통과 (0.30ms, 10.3MB)
테스트 20 〉	통과 (0.30ms, 10.3MB)
'''