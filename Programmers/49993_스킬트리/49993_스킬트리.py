import math
def solution(skill, skill_trees):
    answer = 0
    arr = list(skill)
    for tree in skill_trees:
        branch = list(tree) 
        flag = True
        idx = 0
        # 각 스킬 트리의 요소를 돌아보면서 
        for i in branch:
            # 해당 요소가 skill에 포함되지 않는다면 
            if i not in arr:
                continue
            # 요소가 포함된다면, 스킬에서 몇 번쨰 index인지 파악
            temp = arr.index(i) 
            # 민액 현재 요소의 index와 위치해야 할 index가 다르다면 스킬트리 nope
            if temp != idx:
                flag = False
                break 
            # 현재 위치해야할 index와 현재 요소의 index가 동일하다면 다음으로 갑시다!
            else:
                # index를 1 추가함으로써, 다음 스킬트리 요소의 index가 다음 스킬 요소인지 확인할 수 있다.
                idx += 1
        if flag:
            answer += 1
            
    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
'''

'''
T: 45
풀고 나니까 너무 간단한데.. 중간중간 구현하다 2번 실패했다. 
그래서 다시 풀고 또 풀고 그랬다!! 
처음부터 제대로 생각하고 고민해보자. 
'''