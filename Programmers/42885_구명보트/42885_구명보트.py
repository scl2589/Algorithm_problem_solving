'''
한 번에 최대 2명 
무게 제한을 넘지만 않으면 된다.
'''
def solution(people, limit):
    answer = 0
    people.sort() 
    start = 0 
    leftover = 0
    end = len(people) - 1
    while start <= end:
        if people[start] + people[end] <= limit: 
            answer += 1
            start += 1 
            end -= 1
        else:
            leftover += 1
            end -= 1
    return answer + leftover

'''
T: 30분
- 정확히 30분 걸렸다. 
- 초반에는 무게 제한을 넘지 않으면서, 무게 제한과 같아야만 보트를 탈 수 있다고 착각해서 굉장한 삽질을 했다.
- 그 이후, 무게 제한을 넘지 않아도 된다는 것을 깨달았고, 금방 풀었다.
- 해당 문제를 풀기 위해 투포인터를 사용하였다.
'''