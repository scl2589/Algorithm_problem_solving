# import sys

# sys.stdin = open('input.txt')
for tc in range(1, 11):
    n, nums = map(int, input().split())
    nums = list(str(nums))

    result = True
    while result == True:
        count = 0
        for i in range(len(nums)-1):
            correct = len(nums)-1
            count += 1
            if nums[i] == nums[i+1]:
                del nums[i:i+2]
                break
        if count == correct:
            result = False

    print('#{} {}'.format(tc,''.join(nums)))

# example