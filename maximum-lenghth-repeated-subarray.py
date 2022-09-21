"""Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays."""

# nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# 3     #[3, 2, 1]

# solve this as an 2d array problem
# we want to create a matrix:
"""
if (num1[i] == nums2[j]) -> that's a matching case! So we want to update dp[i][j] = dp[i-1][j-1] + 1;
dp[i][j] =

0 [] 1 2 3 2 1
[]0  0 0 0 0 0 
3 0  0 0 1 0 0
2 0  0 1 0 2 0
1 0  1 0 0 0 3 
4 0  0 0 0 0 0
7 0  0 0 0 0 0
"""

# start with [] to avoid unecessary if conditions in the code and it also already deals with empty lists.
# will take 2 pointers, to iterate over nums1 and nums2. whenever I find a nums1[i] that is the same as nums2[j], i will update the dp value to whatever value is in dp[i-1][j-1] + 1.
# will keep storing the max_count to the longest length and at the end will return it


def findLength(nums1, nums2):

    #create a dp /2d array.
    N, M = len(nums1), len(nums2) # len of lists
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]  # dp arr initialize with extra empty spot to handle exceptions
    output = 0  # count of subarray len
    for i in range(1, N+1): # loop through both arrays starting at index 1 since we had one extra in the dp
        for j in range(1, M+1):
            if nums1[i-1] == nums2[j-1]:    # if we have a match, add 1 to whatever number we have in the prev row and col
                dp[i][j] = 1 + dp[i-1][j-1] # increment the amount in our dp table of matching nums from both arrays
            output = max(output, dp[i][j])
    return output 



    return 
print(findLength([1,2,3,2,1], [3,2,1,4,7]))

# https://www.youtube.com/watch?v=BgLVRkA8w6w -code from there
# https://www.youtube.com/watch?v=hmXH7MzcGv4 - better understending