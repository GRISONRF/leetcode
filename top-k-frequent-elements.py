# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.



def topKFrequent(nums):
    # creating a dictionary - key = number, value = how many times this number appears
    # ***** i am not sure if i can add/modify numbers to the value of a dictionary [google]
    
    # return the k greatest values.
    
    # input => [1, 1, 1, 1, 2, 2, 2, 3] k=2
    # output => [1, 2]
    
    #if nums only has one number
    if len(nums) == 1:
        return [nums[0]]
            
    #creating a count for how many times n appears in nums
    count = {} # => {1:4, 2:3, 3:1} //// {-1:2}

    # iterate through nums
    for n in nums:
        #every time it founds n in nums, add 1 to the count[n]
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
            
    if len(count) == 1:
        return count.keys()
            
    # key = number / value = how many times
    # return the key that has the greates value.
    
    #list to hold the values
    value_holder = [] #=> [1, 2, 3]
    #return the k greatest values in count [python dict documentation]
    for k, v in count.items():   #=> 1:4
        #add values to list
        value_holder.append(k)
        
    # return the k highest
    value_holder.sort() #[1, 2, 3]
    return value_holder[:k-1]
        
                
print(topKFrequent([1,2])) #2
print(topKFrequent([1,1,1,2,2,3])) # [1,2]
print(topKFrequent([1])) #1
        
        