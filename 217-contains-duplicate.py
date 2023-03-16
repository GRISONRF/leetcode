class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        #true if number appear twice. 
        return len(nums) != len(set(nums))
        #runtime 537ms/memory 28.7MB


        