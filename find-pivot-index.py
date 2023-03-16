def pivotIndex(nums):
    """ find the spot where both left and right side sum is equal and return the index of that spot """

    #calculate total sum of array
    total_sum = sum(nums)

    # #when sum of list - 1st numner = 0, so pivot is number at 1 
    # if total_sum - nums[0] == 0:
    #     return 1
    
    left_sum = 0
    #right_sum total_sum - nums[i] - left_sum
    for i in range(len(nums)):
        right_sum = total_sum - nums[i] - left_sum
        if left_sum == right_sum:
            return i
        else:
            left_sum += nums[i]
    
    return -1
        
        


print(pivotIndex([2, 1, -1]))