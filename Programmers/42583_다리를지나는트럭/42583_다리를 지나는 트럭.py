from collections import deque
def solution(bridge_length, weight, truck_weights):
    q = []
    trucks = [i for i in truck_weights]
    passed = []
    w = 0
    count = 0
    while True:
        # 시간 추가하기 
        count += 1
        # 만약 현재 다리가 꽉 차 있다면 (하나만 추가하면 오버된다면)
        if len(q) > bridge_length - 1: 
            popped = q.pop()
            if popped != 0:
                # 마지막에 도착한 것이 0이 아니고 무게가 있다면 건너온 것으로 파악
                passed.append(popped) 
                w -= popped
        # 만약 건너온 트럭의 개수와 총 트럭의 개수가 같다면 끝내기
        if len(passed) == len(truck_weights):
            break
        # 만약 truck의 배열이 존재하고,
        # 다음 다리를 건널 트럭과 현재 다리에 있는 트럭의 무게가 최대 무게를 넘지 않는다면
        elif trucks and w + trucks[0] <= weight:
            truck = trucks.pop(0)
            w += truck 
            q = [truck] + q 
        # 다리의 무게가 최대 무게를 넘는다면 0 추가 
        else:
            q = [0] + q 
        
    return count

'''
테스트 1 〉	통과 (10.57ms, 10.2MB)
테스트 2 〉	통과 (928.07ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (194.61ms, 10.2MB)
테스트 5 〉	통과 (5355.08ms, 10.5MB)
테스트 6 〉	통과 (943.95ms, 10.3MB)
테스트 7 〉	통과 (4.88ms, 10.3MB)
테스트 8 〉	통과 (0.30ms, 10.3MB)
테스트 9 〉	통과 (5.74ms, 10.2MB)
테스트 10 〉	통과 (0.40ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.55ms, 10.3MB)
테스트 13 〉	통과 (2.03ms, 10.2MB)
테스트 14 〉	통과 (0.07ms, 10.3MB)
'''

# 20배 가량 빠른 코드 - 다시 푼 버전 
def solution(bridge_length, weight, truck_weights):
    q = [0]*bridge_length
    idx = 0
    w = 0
    count = 0
    while True:
        # 시간 추가하기 
        count += 1
        # 만약 현재 다리가 꽉 차 있다면 (하나만 추가하면 오버된다면)
        w -= q.pop(0)
        if idx < len(truck_weights):
            # 다음 다리를 건널 트럭과 현재 다리에 있는 트럭의 무게가 최대 무게를 넘지 않는다면
            if w + truck_weights[idx] <= weight:
                w += truck_weights[idx] 
                q.append(truck_weights[idx])
                idx += 1
            # 다리의 무게가 최대 무게를 넘는다면 0 추가 
            else:
                q.append(0)
        else:
            count += bridge_length - 1
            break
        
    return count

'''
테스트 1 〉	통과 (0.85ms, 10.2MB)
테스트 2 〉	통과 (44.76ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (11.56ms, 10.3MB)
테스트 5 〉	통과 (298.08ms, 10.3MB)
테스트 6 〉	통과 (48.55ms, 10.3MB)
테스트 7 〉	통과 (0.89ms, 10.2MB)
테스트 8 〉	통과 (0.13ms, 10.2MB)
테스트 9 〉	통과 (3.42ms, 10.1MB)
테스트 10 〉	통과 (0.67ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.29ms, 10.3MB)
테스트 13 〉	통과 (1.18ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
'''