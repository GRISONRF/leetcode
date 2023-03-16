class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #numbers = [2,7,11,15], target = 9


        # map = {}

        # for i, v in enumerate(numbers):
        #     inc = target - v

        #     if inc not in map:
        #        map[v] = i

        #     else:
        #         return [map[inc] + 1, i + 1 ]

        l = 0
        r = len(numbers) - 1

        #while the left is not greater than right, 
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l+1, r+1]

                