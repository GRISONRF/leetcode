# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# input -> s = "anagram",, t = "nagaram"
# output -> True

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         new_s = sorted(s)
#         new_t = sorted(t)
#         if new_s == new_t: 
#             return True
#         else:
#             return False



def isAnagram(s, t):

    if len(s) != len(t):
        return False

    all_char = {}

    for char in s:
        if char not in all_char:
            all_char[s] = 1
        all_char[s] += 1

    for char2 in t:
        if char2 not in all_char:
            return False
        return True


print(isAnagram("anagram", "nagaram"))