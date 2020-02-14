import sys

T = int(sys.stdin.readline())
stack = []

for _ in range(T):
    D = int(sys.stdin.readline())

    if D == 0:
        if len(stack) != 0:
            stack.pop()
    else:
        stack.append(D)
print(sum(stack))