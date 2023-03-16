class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #approach: use prefix and suffix products to calculate the product of all elements in the array except for the current element at the given index.

        # -> the prefix product of an element is the product of all elements to its left in the array. Ex: if nums = [1,2,3,4] the prefix product is [1,1,2,6] where prefix[0]=1, prefix[1]=1 (1), prefix[2]= 2 (1*2) and prefix[3]= 6 (1*2*3)
        # -> suffix product of an element is the product of all elements to its right in the array. if nums=[1,2,3,4], suffix product is [24,12,4,1] where suffix[3]=1, suffix[2]=4 (4*1), suffix[1]=12 (3*4), suffix[0]=24 (2*3*4)

        #we will find the prefix and suffix for every number, so if we want to find the product of all elements ecept self, we just need to multiply the suffix and prefix of this number.
        

        #create a list of prefix, sufix and ans with empty 'spaces' 
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        ans = [1] * len(nums)

        #calculating prefix
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        #calculating sufix / going  backwards
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        #calculating the answer
        for i in range(len(nums)):
            ans[i] = prefix[i]*suffix[i]

        return ans