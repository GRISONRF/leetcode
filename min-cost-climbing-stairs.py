""" You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor. """



def minCostClimbingStairs(cost):

    #append 0 because that's what we want to reach
    cost.append(0)

    #iterate through array in reverse order. we want to start at -3 because we already know the last number is now 0 and the second last number doesnt change its cost.
    for i in range(len(cost) -3, -1, -1):
        # want to keep adding the minimum cost to get to the top of stair
        cost[i] += min(cost[i + 1], cost[i + 2])
        # cost[i] += min(cost[i] + cost[i+1], cost[i] + cost[i+2]) #[10, 15, 20, 0] -> (15 + 20-single jump, 15 + 0-doble jump) menor numero entre os dois vai ser igual ao const[i]. continua fazendo isso a cada iteração e no fim retorna o menor numero de todos
    return min(cost[0], cost[1] )
        


print(minCostClimbingStairs([10,15,20]))
print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))