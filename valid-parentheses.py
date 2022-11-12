""" Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type. """



def isValid(s):

    all_char = {")" : "(", "}" : "{", "]" : "["}
    open_char = all_char.values()
    track_char = []

    if len(s) % 2 != 0:
        return False

    for char in s:

        #if the char is a closing symbol
        if char in all_char:
            
            #if there is a track list (not empty) and the last item IS the open one, pop it from the track
            if track_char and track_char[-1] == all_char[char]:
                track_char.pop()
            else:
                return False
        elif char in open_char:
            track_char.append(char)

    return len(track_char) == 0
        

            


print(isValid("){"))
print(isValid("()[]"))