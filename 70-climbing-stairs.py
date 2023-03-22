class Solution:
    def climbStairs(self, n: int) -> int:
        """ we are going backwards, so starting at the end. we know the 2 last numbers are 1 and 1 (because there is only 1 way to get to the end by both positions) and so we just need to keep adding the 2 "pointers" together to find the result of the previous number """


        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = temp + two
            two = temp

        return one
