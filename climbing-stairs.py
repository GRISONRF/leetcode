"""You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

https://leetcode.com/problems/climbing-stairs/
"""


def climbStairs(n):
    
    one = 1
    two = 1 

    for i in range(n-1):
        #set this temporary holder for one, so when we set two = one it gets the first value and not the updated one
        temp = one
        # set one to be igual one + two (1 step plus 2 steps)
        one = one + two
        # now two is igual to the last value of number one.
            # that is what makes the 'pointers' to move, so we are always counting the 1 and 2 steps to get to the value of n.
        two = temp

    return one


print(climbStairs(2))
print(climbStairs(3))
