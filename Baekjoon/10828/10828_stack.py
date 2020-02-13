'''

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys
input = sys.stdin.readline

class Stack():
    def __init__(self):
        self.data = []

    def push(self, a):
        self.data.append(a)

    def pop(self):
        if len(self.data) != 0:
            return self.data.pop()
        else:
            return -1
    
    def size(self):
        return len(self.data)

    def empty(self):
        if self.data:
            return 0
        else:
            return 1
    
    def top(self):
        if not self.empty():
            return self.data[-1]
        else:
            return -1

N = int(input())
stack1 =  Stack()
for tc in range(N):
    commands = list(map(str, input().split()))
    if commands[0] == 'push':
        stack1.push(int(commands[1]))
    elif commands[0] == 'top':
        print(stack1.top())
    elif commands[0] == 'empty':
        print(stack1.empty())
    elif commands[0] == 'pop':
        print(stack1.pop())
    elif commands[0] == 'size':
        print(stack1.size())
    