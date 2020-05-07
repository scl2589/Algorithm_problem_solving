T = int(input())
for tc in range(1, T+1):
    #N:컨테이너 수, M: 트럭 수
    N, M = map(int, input().split())
    #freight_weight: N개의 화물의 무게, loading_capacity:M개 트럭의 적재용량
    freight_weight = list(map(int, input().split()))
    freight_weight.sort(key=lambda x: -x)
    loading_capacity = list(map(int, input().split()))
    loading_capacity.sort(key=lambda x: -x)
    total_weight = 0
    for i in loading_capacity:
        for j in freight_weight:
            if i >= j:
                total_weight += j
                freight_weight.remove(j)
                break
    print('#{} {}'.format(tc, total_weight))
