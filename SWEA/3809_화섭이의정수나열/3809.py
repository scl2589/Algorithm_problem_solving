import math
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = []
    while len(cards)!=N:
        cards.extend(input().split())

    i = 0
    this_number = True
    while this_number:
        #찾아야 될 숫자 string으로 변환
        strings = list(str(i))
        for a in range(len(cards)):
            if cards[a] == strings[0]:
                if cards[a:a+len(strings)] == strings:
                    break
                else:
                    continue
        else:
            print('#{} {}'.format(tc, i))
            this_number = False

        i += 1
