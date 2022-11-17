""" Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty. """

def backspaceCompare(s,t):

        """ create 2 empty "texts" to store the 'result' of both strings
        for each at s, add at text, if see a #, pop()
        same for t
        compare both     
        """

        text1 = []
        text2 = []

        for i in s:
            if text1 and i == '#':
                text1.pop() 
            else:
                text1.append(i)
        
        for i in t:
            if text2 and i == '#':
                text2.pop() 
            else:
                text2.append(i)
                       
        return text1 == text2

print(backspaceCompare("a##c","#a#c" ))