# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 
#JavaScript

const twoSum = (nums, target) => {
  const map = {};

  for (let i = 0; i < nums.length; i++) {
    const another = target - nums[i];

    if (another in map) {
      return [map[another], i];
    }

    map[nums[i]] = i;
  }

  return null;
};


#################################################

#Python

# nums = [3, 2, 4]
# target = 6

# target - a = b
# return index of a and b

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      
      dict = {}
      for i, n in enumerate(nums):   #=> 0, 3
          remained_value = target - n
          if remained_value in dict:
              return [dict[remained_value], i]
          else:
              dict[n] = i

