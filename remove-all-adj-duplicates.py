"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
"""

def removeDuplicates(s, k):
    #create a stack to keep track of the character and count

    #iterate through s
        #check if the stack is empty and if the last character is the same as the one we are iterating.
            #if so, add 1 to the counter
            #else, means the last letter is not consecutive to the new one, so we add it to the stack with the counter as 1
        #if we the counter in the stack with the iterated letter is >= to s, we want to pop it.

        #take the stack and convert it to the result string by iterating throught the stack and multiplying the char to the counter left in the stack
    
    
    stack = [] # char, counter

    for c in s:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1
        else:
            stack.append([c, 1])

        if stack[-1][1] == k:
            stack.pop()
    
    res = ""
    for char, count in stack:
        res += (char * count)
    return res



print(removeDuplicates("aaabbbacd", 2))