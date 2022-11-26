""" You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits. """



def plusOne(digits):
    #invert order of digits
    digits = digits[::-1]
    #create a var for the carried 1 and other to iterate
    one, i = 1, 0

    #iterate throught the list just until one is not 1 anymore
    while one:
        #make sure i is going to be lass than length
        if i < len(digits):
            #if the digit is iqual to 9, it will now be 0 (because we "added" 1 to it) and since one is still =1, it will either fall into the else, add 1 and stop, or keep changing 9 for 0 until it ends.
            if digits[i] == 9:
                digits[i] = 0
            #else, just add 1 to it, and change one to 0, because we didn't 
            else: 
                digits[i] += 1
                one = 0
        #if the list is empty, just at 1 to it and finish the loop
        else: 
            digits.append(1)
            one = 0
        #add 1 to i, so it iterates through the list
        i += 1
            
    #return the list in right order
    return digits[::-1]

    



print(plusOne([1, 2, 3]))
print(plusOne([9, 9, 9]))