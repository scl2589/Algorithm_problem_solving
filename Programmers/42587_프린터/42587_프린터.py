'''
중요도가 높은 문서를 먼저 인쇄하는 프린터 개발.
1. 가장 앞에 있는 문서 J를 대기 목록에서 꺼낸다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기 목록의 가장 마지막에 넣는다.
3. 그렇지 않으면 J를 인쇄한다.

숫자가 클수록 중요하다는 뜻. 
'''

from collections import deque 

def solution(priorities, location):
    answer = 0
    q = deque(i for i in priorities)
    while q:
        current = q.popleft()
        # 뒤에 중요도가 더 높은 문서가 있는지 확인
        flag = False
        for i in q:
            if i > current: 
                flag = True
                break
        # 뒤에 중요도가 높은 문서가 있을 경우
        if flag:
            q.append(current)
            location -= 1 
            if location == -1:
                location = len(q) - 1
        # 현재 문서의 중요도가 가장 높을 경우
        else:
            # 만약 내가 찾고자 하는 문서의 위치가 현재 문서라면 answer 반환
            if location == 0:
                return answer + 1
            # 내가 찾고자 하는 문서의 위치가 현재 문서가 아니라면 
            else:
                location -= 1
                if location == -1:
                    location = len(q) - 1
                answer += 1

'''
테스트 1 〉	통과 (0.15ms, 10.2MB)
테스트 2 〉	통과 (0.36ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.06ms, 10.3MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
테스트 8 〉	통과 (0.26ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.07ms, 10.2MB)
테스트 11 〉	통과 (0.20ms, 10.1MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.18ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.03ms, 10.2MB)
테스트 17 〉	통과 (0.25ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.22ms, 10.3MB)
테스트 20 〉	통과 (0.04ms, 10.2MB)
'''

# any 활용 코드
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
'''
테스트 1 〉	통과 (0.54ms, 10.2MB)
테스트 2 〉	통과 (1.19ms, 10.2MB)
테스트 3 〉	통과 (0.07ms, 10.1MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.17ms, 10.2MB)
테스트 7 〉	통과 (0.15ms, 10.2MB)
테스트 8 〉	통과 (1.13ms, 10.1MB)
테스트 9 〉	통과 (0.03ms, 10MB)
테스트 10 〉	통과 (0.18ms, 10.2MB)
테스트 11 〉	통과 (0.63ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
테스트 13 〉	통과 (0.63ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.1MB)
테스트 16 〉	통과 (0.07ms, 10.3MB)
테스트 17 〉	통과 (0.82ms, 10.2MB)
테스트 18 〉	통과 (0.03ms, 10.1MB)
테스트 19 〉	통과 (0.66ms, 10.2MB)
테스트 20 〉	통과 (0.11ms, 10.2MB)
'''