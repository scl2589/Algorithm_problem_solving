def findRoot(x, root):
    if parent[x] == 1:
        root.append(1)
        return
    root.append(parent[x])
    findRoot(parent[x], root)


def findChild(x):
    global result2
    if child[x]: 
        result2 += len(child[x])
        for i in child[x]:
            findChild(i)
    else:
        return


T = int(input())
for tc in range(1, T+1):
    V, E, num1, num2 = map(int, input().split())
    edges = list(map(int, input().split()))
    parent = [-1] * (V+1)
    child = [[] for _ in range(V+1)]
    for i in range(0, len(edges), 2):
        parent[edges[i+1]] = edges[i]
        child[edges[i]].append(edges[i+1])
    root1 = [num1]
    root2 = [num2]
    findRoot(num1, root1)
    findRoot(num2, root2)
    root1 = root1[::-1]
    root2 = root2[::-1]
    result1 = 0
    result2 = 1
    for i in range(len(root1)):
        if root1[i] != root2[i]:
            result1 = root1[i-1]
            break
    findChild(result1)
    print(f'#{tc} {result1} {result2}')



    