while True:
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break
    else:
        if nums[0]**2 + nums[1] **2 == nums[2]**2 or nums[1]**2 + nums[2]**2 == nums[0]**2 or nums[0]**2 + nums[2]**2 == nums[1]**2:
            print('right')
        else:
            print('wrong')