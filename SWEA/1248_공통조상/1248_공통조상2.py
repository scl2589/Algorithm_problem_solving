def find_parent(n, parent_list):
    parent = tree[n][2]
    if parent:
        parent_list.append(parent)
        return find_parent(parent, parent_list)
    else:
        return parent_list
 
def count_sun(n):
    global cnt
    if tree[n][0]:
        if tree[n][1]:
            cnt += 1
            count_sun(tree[n][1])
        cnt += 1
        count_sun(tree[n][0])
    else:
        return
 
 
 
T = int(input())
for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    L = list(map(int, input().split()))
    #   왼쪽 오른쪽 부모
    # 1
    # 2
    # 3
    tree = [[0]*3 for _ in range(V+1)]
    for i in range(E):
        parent = L[2*i]
        sun = L[2*i + 1]
        if not tree[parent][0]:
            tree[parent][0] = sun
        else:
            tree[parent][1] = sun
        tree[sun][2] = parent
 
    parent_list1 = find_parent(n1, [])
    parent_list2 = find_parent(n2, [])
    minv = min(len(parent_list1), len(parent_list2))
    for k in range(1, minv+1):
        if parent_list1[-k] != parent_list2[-k]:
            result = parent_list1[-k+1]
            break
    else:
        result = minv
    cnt = 1
    count_sun(result)
    print('#{} {} {}'.format(tc, result, cnt))