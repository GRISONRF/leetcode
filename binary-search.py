"""Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity."""

from operator import indexOf


def search(nums, target):

    # l, r = 0, len(nums) - 1 #setting 2 pointers, left is the first element (0) right is the last element len(nums) - 1 **INDEX**)

    # if target not in nums:
    #     return -1

    # # we want to keep going until we check all the numbers / there is no more possibilities for us to get the result
    # while l <= r:  #left pointer cant cross/pass the right pointer! 
    #     #find the middleway point
    #     m = (l + r) // 2 #m=2
        
    #     if nums[m] > target: #if m is greater than target, means we passed the target, so we want to look on left side
    #         r = m - 1
    #     elif nums[m] < target:
    #         l = m + 1
    #     else:
    #         return m

        if target not in nums:
            return -1

        left = 0 
        right = len(nums) - 1
        

        while left <= right:
            pointer = (right + left) // 2
            
            if nums[pointer] > target:
                right = pointer - 1
            elif nums[pointer] < target:
                left = pointer + 1
            else: return pointer
        return -1

# target is 5
# m = 2
print(search([-1,0,3,5,9,12], 2))