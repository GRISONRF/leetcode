def generateParenthesis(n):
    """ 
    create a stack to store the parentesis. so will only add a closed if there is a open one
    
    add open parenthesis while open < n
    add a closing if open > closed
    at the end, its only valid if open == closed == n

    recursive, so it will call it self with the updates values for open and/or close
    """

    stack = []
    ans = []

    def countParent(open, close):
        #to when we stop the recursion and return the result.
        #this will happend when we use the n times for the open and closed parentesis
        #we will append to res what we have in the stack
        if open == close == n:
            ans.append("".join(stack))
            return

        #open < n because we will only add until we have n*(
            #add the open ( to the stack
            #call the function again but add 1 to open
        if open < n:
            stack.append("(")
            countParent(open+1, close)
            stack.pop()
        
        if close < open:
            stack.append(")")
            countParent(open, close+1)
            stack.pop()

    countParent(0,0)
    return ans


print(generateParenthesis(3))