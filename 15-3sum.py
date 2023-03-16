class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """ sort the array
        iterate
        check if there are any duplicate number and ignore it if yes
        deal with the rest as the 2sum code, using 2 pointers in a nested loop, using r, l and the first iteration variable
         """

        ans = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            

            l, r = i + 1, len(nums) - 1
            while l < r:
                tree_sum = n + nums[l] + nums[r]
                if tree_sum > 0:
                    r -= 1
                elif tree_sum < 0:
                    l += 1
                else:
                    ans.append([n, nums[l], nums[r]])

                    #only need to increment one pointer because the conditions will deal with changing the other/both pointers during the code.
                    l += 1
                    while nums[l] == nums[l-1] and l< r:
                        l += 1
        return ans
