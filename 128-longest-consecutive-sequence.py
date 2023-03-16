class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """
        T: O(n)  M: O(n)
        to know if we're dealing with a subset of consecutive elements, we can:
        for each item, check if the previous item is in the list, if not, that is the first element in the subarray, now we look for the item+1 in the array until we can't find it anymore. when there is no more item+1, we check if the len is greatest than the current max len and try to find the next subarray. for the time complexity to be lower, we change the array to a set first 
        
        to identify the begining or end of a subset: is has no left/right neighbor

        """


        #check if this number is the start of a sequence
        #if this number doesnt have a left neighbor, means it's the first number in the sequence
        #jeeo checking the consecutive numbers to know if they exist in the nums array
        #we already know n is the first number in the subarray, so now we keep iterating while the next number is in nums. length starts at 0 we add 1 to the length every iteration, which is how we find the consecutive numbers after the first element in the subarray
        #as the length grow we will check more consecutive numbers
        #keep updating the maX_len in case we found the longest subsequece

        #make nums into a set to make it faster
        num_set = set(nums)
        #store max_len found so far  
        max_len = 0 
        
        # [100,4,200,1,3,2]

        for n in nums:  #use nums in case there are duplicates and to preserve the order

            #if left neighbor is NOT in num_set means its the first item in the subarray
            if (n - 1) not in num_set:
                #initialize lenght that will change at every iteration
                length = 0
                
                # get the consecutive numbers if exist in the set
                while (n + length) in num_set:
                    length += 1
                #update the max if needed
                max_len = max(max_len, length)   
                #if there isnt a consecutive number of n in nums
            
        return max_len


            

        
                
