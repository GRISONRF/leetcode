""" Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer. """


def maxProduct(nums):
        
    """
    edge case if num is empty, return 0

    set up variables for
    max num so far starting at the first
    min num so far starting at the first
    result starting at the first

    --thats because we need to compare the first number to the rest, and if there is only one number in the array, thats what will be returned
        
            
    for each num in nums starting at the second number
        max so far = max(result, maxsofar * num, minsofar * num)
        min so far = min(result, maxsofar * num, minsofar * num)
        result = max(minsofar, maxsofar)

        *** need to create a tempmaxsofar because if we don't, at the min so far we will be using the max at that iteration, and not from the previous one
            
    return result    """

    if not nums:
        return 0
    
    maxSoFar = nums[0]
    minSoFar = nums[0]
    result = nums[0]

    for num in nums[1:]:
        tempMaxSoFar = max(num, num * maxSoFar, num * minSoFar)
        minSoFar = min(num, num * maxSoFar, num * minSoFar)
        maxSoFar = tempMaxSoFar
        result = max(maxSoFar, result)


    return result


    
print(maxProduct([2,3,-2,4]))
print(maxProduct([-1]))
print(maxProduct([0,2]))
print(maxProduct([-2,0,1]))
