""" We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

  """

from curses.ascii import isupper


def detectCapitalUse(word):

    if (word[0].isupper() and word[1:].islower()) or word.isupper() or word.islower():
        return True
    else:
        return False


print(detectCapitalUse('FlaG'))