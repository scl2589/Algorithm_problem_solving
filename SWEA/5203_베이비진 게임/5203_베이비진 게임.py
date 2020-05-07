def check(deck):
    deck.sort(key= lambda x: x)
    #트리플 확인
    for i in range(len(deck)-2):
        if deck[i] == deck[i+1] and deck[i+1] == deck[i+2]:
            return True
    #런 확인
    for i in range(len(deck)-2):
        if deck[i]+1 == deck[i+1] and deck[i+1]+1 == deck[i+2]:
            return True
    else:
        return False
 

T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))
    player1=[]
    player2=[]
    for i in range(len(num)):
        if not i % 2:
            player1.append(num[i])
            if len(player1)>=3:
                if check(player1):
                    print('#{} 1'.format(tc))
                    break
        else:
            player2.append(num[i])
            if len(player2)>=3:
                if check(player2):
                    print('#{} 2'.format(tc))
                    break
    else:
        print('#{} 0'.format(tc))
