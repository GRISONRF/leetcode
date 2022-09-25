""" Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order. """



def reverseWords(s):

    new_sent = s.split()
    print(new_sent)
    rev_sent = ""
    for char in new_sent:
        rev_sent += char[::-1] + " "
    print(rev_sent)


    




reverseWords("Let's take LeetCode contest")