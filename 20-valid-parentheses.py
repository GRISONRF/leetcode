class Solution:
    def isValid(self, s: str) -> bool:
        """ 
        valid:
        {}[]()
        ([{}])
        []

        input: string
        output: boolean

        if string is valid or not
        -> "()"
        -> true

        stack store the previous paren

        iterate string. #check if its valid
            if the closed pare has an open of the same type in the stack: # [true]
                remove the open pare from the stack
            if a close paren and there's no open or not same type:
                return false
            if a open paren:
                add to the stack

        if stack is empty, return true. else false
        
        O(n)
        """

        stack = []
        paren = {')':'(','}':'{',']':'['}

        for p in s:
            if p in paren: # p == ")" or p == "]" or p == "}":  # p = ]
                if stack and stack[-1] == paren[p]: #if matching pare
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(p)
        # print(stack)

        if stack:
            return False
        else:
            return True







