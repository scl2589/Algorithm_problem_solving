T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 순번과 함께 list 만든 후,  정렬
    atm = [[i, idx+1] for idx, i in enumerate(arr)]
    atm.sort(key = lambda x: x[0])

    # accumulate할 total 배열과, 정답인 total 선언 
    totals= [atm[0][0]]
    total = atm[0][0]

    # atm 배열을 돌면서 sum을 추가하기
    for i in range(1, len(atm)):
        total += totals[-1] + atm[i][0]
        totals.append(totals[-1] + atm[i][0])
    print(f'#{tc} {total}')

