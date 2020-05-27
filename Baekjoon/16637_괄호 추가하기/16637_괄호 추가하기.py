def calc(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2


def f(i, total, N, eq):
    global maxV
    if i >= N:
        maxV = max(total, maxV)
    else:
        # 괄호 없이 계산한다.
        calculated = calc(total, int(eq[i+1]), eq[i])
        f(i + 2, calculated, N, eq)
        # 현재 index 다음에 괄호를 추가해, 그 연산을 계산한 후, 현재의 값과 계산한다.
        # 3 + 8 * 7 - 9 * 2라고 할 때, 현재 내가 +의 위치라면, 8을 그냥 더할지, 혹은 괄호를 씌워서 (8*7)을 더할지 결정한다.
        # 위코드는, 8을 그냥 더하는 것이고, 아래는 괄호를 씌워서 계산을 하는 것이다.
        if i + 4 <= N:
            calculated = calc(total, calc(int(eq[i+1]), int(eq[i+3]), eq[i+2]), eq[i])
            f(i+4, calculated, N, eq)


N = int(input())
eq = list(input())
maxV = float('-inf')
f(1, int(eq[0]), N, eq)
print(maxV)