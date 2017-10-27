def sortColors(nums):
    i = 0
    j = 0

    for cur in range(len(nums)):
        n = nums[cur]
        nums[cur] = 2

        if n < 2:
            nums[j] = 1
            j += 1

        if n < 1:
            nums[i] = 0
            i += 1

    return nums

nums = [0,2,1,0,2,1,1]
print sortColors(nums)