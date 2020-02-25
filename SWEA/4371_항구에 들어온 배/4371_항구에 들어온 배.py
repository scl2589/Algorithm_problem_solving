T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = [int(input()) for _ in range(N)]

    result = []
    for i in range(1, N-1):
        if result:
            for r in result:
                if not (nums[i]-1) % r:
                    break
            else:
                result.append(nums[i]-1)
        else:
            result.append(nums[i]-1)
    if len(nums) == 1:
        result.append(1)
    print('#{} {}'.format(tc, len(result)))


#
# for t in range(int(input())):
#     N=int(input())
#     Nice_boat = []
#     X = int(input())
#     for _ in range(N-1):
#         Z=int(input())
#         if Nice_boat == []:
#             Nice_boat.append(Z-X)
#         else:
#             for i in Nice_boat:
#                 if (Z-X)%i==0:
#                     break
#             else:
#                 Nice_boat.append(Z-X)
#     print('#{0} {1}'.format(t+1,len(Nice_boat)))