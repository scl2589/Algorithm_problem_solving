# 메모리 제한이 있기 떄문에
# 미리 10,000이 들어갈 수 있는 list를 만들어준 뒤, 하나씩 더해주고, 메모리에서 없애버리는 방식을 사용한다.
# 숫자의 위치와 인덱스 값을 일치시키면, 숫자를 저장할 필요 없이 인덱스 값을 불러오면 됩니다.
# 마지막 for문에서 리스트의 앞에서부터 값이 있는 숫자들을 차례로 출력합니다.

import sys
N = int(sys.stdin.readline())
arr = [0 for _ in range(100001)]
for _ in range(N):
    arr[int(sys.stdin.readline())] += 1

for i in range(10001):
    if arr[i] > 0:
        for _ in range(arr[i]):
            print(i)