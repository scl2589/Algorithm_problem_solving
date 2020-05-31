def subnode(node):
    cnt=0
    c = [node]
    while c:
        cnt+=1
        ch = c.pop(0)
        c+=arrp[ch][1]
    return cnt
def find_p(node):
    p=[0]*(V)  #높이 최대값 v
    p[0]=node
    i=0
    while arrp[p[i]][0]:
        p[i+1]=arrp[p[i]][0]
        i+=1
        if i >=V:
            break
    return p
for t in range(int(input())):
    V, E, N1, N2 = map(int,input().split())
    tree = list(map(int,input().split()))  # 간선은 항상 부모 자식 순으로 표기됨
    arrp = [[0,[]] for _ in range(V+1)]
    for i in range(0,len(tree),2):
        arrp[tree[i+1]][0]=tree[i]
        arrp[tree[i]][1].append(tree[i+1])
    P1=find_p(N1)
    P2=find_p(N2)
    flag=0
    for p1 in P1:
        for p2 in P2:
            if p1==p2:
                p=p1
                flag=1
                break
        if flag:
            break
    print('#{} {} {}'.format(t+1,p,subnode(p)))