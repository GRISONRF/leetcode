""" 
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""

""" 
answer = [""]

if n = 6:
    1, 2, fizz, 4, buzz, fizz

iterate n
    for each i, check if its a multiple of 3 or 5, 
    if it is, instead of printing the number, print the appropriate word

"""
class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                i = "FizzBuzz"
                answer.append(i) 
                next
            elif i % 3 == 0:
                i = "Fizz"
                answer.append(str(i))
            elif i % 5 == 0:
                i = "Buzz"
                answer.append(str(i))
            
            else:
                answer.append(str(i))
        
        print(answer)
        return answer
        