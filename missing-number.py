# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missingNumber(nums):
        
    # Input: nums = [3,0,1] => range [0,3] -missing 2
    # Output: 2 -the number missing
    
    
    # check the length of nums
    # get the range of the length of nums
    # compare if all the numbers in the range of nums are in nums
    # if not, that's the missing number! 

    len_nums = len(nums) #=> 3
    numbers = []
    for r in range(len_nums + 1):
        if r not in nums:
            return r
       

missingNumber([0, 1,])