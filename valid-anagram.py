# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# input -> s = "anagram",, t = "nagaram"
# output -> True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_s = sorted(s)
        new_t = sorted(t)
        if new_s == new_t: 
            return True
        else:
            return False