"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1

"""



def singleNumber(numbs):

    dict_for_nums = {}
    for num in numbs:
        if num in dict_for_nums:
            dict_for_nums[num] += 1
        else:
            dict_for_nums[num] = 1
    
    for v, k in dict_for_nums.items():
        if k == 1:
            print(v)



print(singleNumber([4,1,2,1,2]))
