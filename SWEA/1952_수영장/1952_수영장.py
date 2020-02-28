import math
import sys

sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    # 가격과 월별 횟수 받기
    prices = list(map(int, input().split()))
    months = list(map(int, input().split()))

    # 모두 일일 가격을 사용할 경우나, 1달 가격을 사용할 경우:
    res = []
    total = 0
    for i in months:
        if i != 0 and prices[1] < prices[0] * i:
            total += prices[1]
        elif i != 0:
            total += i * prices[0]
    res.append(total)

    # 1년 가격을 사용할 경우
    res.append(prices[3])

    # 3달 이용권을 사용할 경우
    total = 0
    i = 0
    while True:
        if i >= 12:
            break
        for a in range(i, 12):
            if months[a] != 0:
                i = a
                break
        total += prices[2]
        i += 3
    res.append(total)

    # 3달 이용권과 1개월, 그리고 하루 이용권을 같이 사용할 경우
    # 총 몇달이 있는가?
    count = 0
    start = -1
    for i, value in enumerate(months):
        if value > 0 and start != -1:
            count += 1
        elif value > 0 and start == -1:
            count += 1
            start = i
    total_months = count

    #뒤에서부터 3달씩 채우기
    while count != 0:
        total = 0
        difference = total_months - count
        total += math.ceil(difference / 3) * prices[2]
        for i in range(start, start + count):
            if months[i] * prices[0] > prices[1]:
                total += prices[1]
            else:
                total += months[i] * prices[0]
        res.append(total)
        count -= 1

    #앞에서부터 3달씩 채우기
    #count2는 시작 index부터 1씩 늘려간다
    count2 = 0
    while count2 != start+total_months-1:
        total = 0
        for i in range(start+count2, start+total_months):
            if i == start+count2:
                total += math.ceil(count2/3) * prices[2]
            if months[i] * prices[0] > prices[1]:
                total += prices[1]
            else:
                total += months[i] * prices[0]
        res.append(total)
        count2 += 1
    #print(res)
    print('#{} {}'.format(tc, min(res)))