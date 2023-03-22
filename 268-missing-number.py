class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        #count how many numbers are in the array to find n
        #find the number from 0-n that is not in the array

        n = len(nums)
        for number in range(n+1):
            if number not in nums:
                return number


