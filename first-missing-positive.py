""" Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

"""

def firstMissingPositive(nums):
    
    nums.sort()

    if 1 not in nums:
        return 1

    ans = 1
    # iterate through every number in the range of the list.
    # if there is the number 1 in the list, lets check the next number by adding 1 to the ans, that way we can check in the order from the lowest positive number
    for i in range(len(nums)):
        if nums[i] == ans:
            ans +=1
    return ans

            
       
            
        



# print(firstMissingPositive([1,2,0]))
print(firstMissingPositive([3,4,-1,1]))
