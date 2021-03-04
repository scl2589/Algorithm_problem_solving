'''
실패율 정의 - 스테이지에 도달했으나 아직 클리어 못한 플레이어 수/스테이지 도달 플레이어 수 
'''
from collections import Counter
def solution(N, stages):
    percentage = []
    stages.sort()
    total = len(stages)
    counted = Counter(stages)
    for i in range(1, N + 1):
        if i not in counted:
            percentage.append([i,0])
        else:
            current_player = counted[i]
            percentage.append([i, current_player/total])
            total -= current_player
    answer = sorted(percentage, key = lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer