# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.


def findDisappearedNumbers(nums):

 # nums => [1,1,3]  => range[1,3]
        # output => [2]
        
        
        # get length of nums
        # create an empty list to store the numbers that are not in num
        # iterate through nums and check if all the numbers in range of [1,len] are there.
        
        
    num_len = len(nums) #-> 3

    ####Time Limit Exceeded####
#     answer = []
    
#     for n in range(1, num_len + 1):
#             if n not in nums:
#                 answer.append(n)
#     print(answer)


    if set(nums) != set(range(1, num_len + 1)):
        return set(range(1, num_len + 1)) - set(nums)

findDisappearedNumbers([1, 2, 2])



