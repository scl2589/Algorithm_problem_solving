x, y = map(int, input().split())
num_cut = int(input())
arr_for_count = [[1]*y for _ in range(x)]

#가로 세로 commands
arr = [list(map(int, input().split())) for _ in range(num_cut)]

#가로로 자르는 점선은 0으로 시작
#세로로 자르는 점선은 1으로 시작

x_cut = [0]
y_cut = [0]
for i in arr:
    if i[0] == 0:
        y_cut.append(i[1])
        
    elif i[0] == 1:
        x_cut.append(i[1])
x_cut.append(x)
y_cut.append(y)
x_cut.sort()
y_cut.sort()
print('x_cut:',x_cut)
print('y_cut:',y_cut)

i = 0
area = []
while i < len(y_cut)-2:
    for r in range(y_cut[i],y_cut[i+1]):
        j = 0
        
        while j < len(x_cut)-2:
            total = 0
            for c in range(x_cut[j], x_cut[j+1]):
                total += arr_for_count[r][c]
            j += 1
            area.append(total)
    i += 1

print(area)












