num = int(input())
current = 1
layer = 1

while current < num:
    current += layer * 6
    layer += 1

print(layer)