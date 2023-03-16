def kidsWithCandies(candies, extraCandies):

    first_greatest = max(candies)
    ans = []
    for candy in candies:
        print(candy+extraCandies)
        print(first_greatest)
        if (candy + extraCandies) >= first_greatest:
            ans.append("true")
        elif (candy + extraCandies) < first_greatest: 
            ans.append("false")

    return ans
    
print(kidsWithCandies([2,3,5,1,3], 3))