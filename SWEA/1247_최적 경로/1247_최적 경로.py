from itertools import permutations 

# def perm(n, k):
#     global perm_list
#     if n == k:
#         perm_list.append(customer[::]) ###
#         #print(customer) ###
#     else:
#         for i in range(k, n):
#             customer[i], customer[k] = customer[k], customer[i]
#             perm(n, k+1)
#             customer[i], customer[k] = customer[k], customer[i]


T= int(input())
for tc in range(1, T+1):
    N = int(input()) #고객 수
    #회사, 집, 고객 좌표
    coords = list(map(int, input().split()))

    work = (coords[0], coords[1])
    home = (coords[2], coords[3])
    # memo = [[0]*N for _ in range(N)]
    customer = []

    # customer array 따로 만들기
    for i in range(4, len(coords), 2):
        customer.append((coords[i], coords[i+1]))
    
    minV = float('inf')

    # 순열
    for permutation in permutations(customer):
        path = [work, *permutation, home]
        distance = 0
        for i in range(0, len(path)-1):
            distance += abs(path[i][0]-path[i+1][0]) + abs(path[i][1]-path[i+1][1])
            if distance > minV:
                break
        minV = min(minV, distance)

    print(f'#{tc} {minV}')