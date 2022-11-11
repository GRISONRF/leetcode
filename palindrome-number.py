""" Given an integer x, return true if x is a palindrome , and false otherwise. """

def isPalindrome(x):

    # 1001 -> true
    # 2023 -> false

    #one number: true
    #empty: true
    #can have other char

    x = str(x)
    backw = ""

    for i in x[::-1]:
        backw += i
    
    if backw == x:
        return True
    return False
    

## OR, EVEN MORE SIMPLE:

    x = str(x)

    if x == x[::-1]:
        return True
    return False

print(isPalindrome(1091))