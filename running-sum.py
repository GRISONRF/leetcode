# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

def runningSum(nums): 
    
    count = 0
    answer = []
    for n in nums:
        count += n
        answer.append(count)
    print(answer)

runningSum([1,1,1,1,1])