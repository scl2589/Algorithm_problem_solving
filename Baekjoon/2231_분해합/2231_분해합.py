num_int = int(input())
state = False

for current in range(1, num_int):
    sum = current
    for i in str(current):
        sum += int(i)
    if sum == num_int:
        state = True
        break

if state:
    print(current)
else:
    print(0)