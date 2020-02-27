from collections import deque

def operation(numbers, operators):
    global min_num, max_num
    if operators == [0, 0, 0, 0]:
        res = numbers[0]
        if res > max_num:
            max_num = res
        if res < min_num:
            min_num = res

    else:
        for k in range(4):
            if operators[k] != 0:
                a = numbers.popleft()
                b = numbers.popleft()
                operators[k] -= 1
                if k == 0:
                    numbers.appendleft(a + b)
                if k == 1:
                    numbers.appendleft(a - b)
                if k == 2:
                    numbers.appendleft(a * b)
                if k == 3:
                    numbers.appendleft(int(a / b))
                operation(numbers, operators)
                numbers.popleft()
                operators[k] += 1
                numbers.appendleft(b)
                numbers.appendleft(a)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    operators = list(map(int, input().split()))
    numbers = deque(map(int, input().split()))
    min_num = 100000000
    max_num = (-1) * 100000000
    operation(numbers, operators)
    print('#{} {}'.format(tc, max_num - min_num))