def f(n, atoms):
    s = 0
    for _ in range(4001):
        B = {}
        for i in atoms:
            if i[3] != 0:
                if i[2] == 0:
                    i[1] += 1
                elif i[2] == 1:
                    i[1] -= 1
                elif i[2] == 2:
                    i[0] -= 1
                else:
                    i[0] += 1
                key = (i[0], i[1])
                if abs(i[0]) <= 2000 and abs(i[1]) <= 2000:
                    if key not in B:
                        B[key] = i[3]
                    else:
                        s += B[key] + i[3]
                        B[key] = 0
                        i[3] = 0
                        find_a, find_b = key[0], key[1]
                        for k in atoms:
                            if k[0] == find_a and k[1] == find_b and k[2] != i[2]:
                                k[3] = 0
                                break
    return s

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #x, y, direction, energy
    # 상(0), 하(1), 좌(2), 우(3)
    atoms = []
    for _ in range(N):
        x, y, d, e = map(int, input().split())
        atoms.append([x*2, y*2, d, e])
    
    ans = f(N, atoms)
    
    print(f"#{tc} {ans}")