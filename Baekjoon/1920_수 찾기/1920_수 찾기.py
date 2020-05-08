#실패한 코드
"""
import sys
N = map(int, sys.stdin.readline())
nums1 = list(map(int, sys.stdin.readline().split()))
M = map(int, sys.stdin.readline())
nums2 = list(map(int, sys.stdin.readline().split()))
for j in nums2:
    if j in nums1:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
"""
def find(start, end):
    mid = (start + end)//2
    if start >= end:
        return False
    if nums1[mid] == num:
        return True
    elif nums1[mid] > num:
        return find(start, mid)
    else:
        return find(mid+1, end)

#이분 탐색으로 풀어보자.
N = int(input())
nums1 = list(map(int, input().split()))
nums1.sort()
M = int(input())
nums2 = list(map(int, input().split()))

for num in nums2:
    print(1 if find(0, N) else 0)