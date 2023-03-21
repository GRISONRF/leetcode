class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        already_satisfied = 0
        #find already satisfied customers
        for i in range(len(customers)):
            if grumpy[i] == 0:
                already_satisfied += customers[i]
                customers[i] = 0
        print(already_satisfied)
        print(customers)

            
        #find the most satisfied customers we can get
        cur_satisfied = 0
        max_satisfied = 0

        for i, customer in enumerate(customers):
            cur_satisfied += customer

            if i >= minutes:
                cur_satisfied -= customers[i-minutes]
            max_satisfied = max(max_satisfied, cur_satisfied)

        return max_satisfied + already_satisfied    

