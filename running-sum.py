# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

def runningSum(nums):
    
    # iterate through the list
    # save the number in a count
    #for each iteration, sum with the next number and 
    
    
    count = 0
    answer = []
    for n in nums:
        count += n
        answer.append(count)
    print(answer)

runningSum([1,1,1,1,1])