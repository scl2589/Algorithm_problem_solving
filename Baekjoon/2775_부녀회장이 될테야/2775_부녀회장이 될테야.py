for tc in range(1, int(input())+1):
    # k: 층수 , n: 호수
    k = int(input())
    n = int(input())
    floor = []
    first_floor = [i for i in range(1, n+1)]
    floor.append(first_floor)
    for i in range(1, k+1):
        temp = []
        for j in range(n):
            temp.append(sum(floor[i-1][:j+1]))
        floor.append(temp)
    print(floor[k][n-1])