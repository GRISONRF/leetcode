def numIdenticalPairs(nums):
    """ find the numbers that are a pair """

    counter = 0
    pointer1 = 0
    pointer2 = 1

    while pointer2 <= len(nums) -1:
        if nums[pointer1] == nums[pointer2]:
            counter += 1
        pointer2 += 1
        
        if pointer2 == len(nums):
            pointer1 += 1
            pointer2 = pointer1 +1
    return counter


print(numIdenticalPairs([1,2,3,1,1,3]))