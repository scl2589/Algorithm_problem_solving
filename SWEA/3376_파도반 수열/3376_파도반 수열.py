# def Padovan(n):
#     if n == 1:
#         return 1
#     elif n <= 3:
#         return 1
#     else:
#         return Padovan(n-3) + Padovan(n-2)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     print('#{} {}'.format(tc, Padovan(n)))


T = int(input())
for tc in range(1, T+1):
    arr = [1, 1, 1]
    n = int(input())
    if n <= 3:
        print('#{} {}'.format(tc, arr[n-1]))
    else:
        for i in range(n-3):
            arr.append(arr[-3]+arr[-2])
        print('#{} {}'.format(tc, arr[n-1]))