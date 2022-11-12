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

""" for sorted solution uses less extra memory, but the time complexity is higer.
memory is O(1) but time complexity is 

for second solution MEMORY COMPLEXITY is O(n) because we are using a for loop interating throught the strings. MEMORY COMPLEXITY is also O(n) because we are building 2 new hashmaps

"""

##first answer is slower because uses sorted, so it is 



def isAnagram(s, t):

    if len(s) != len(t):
        return False

    countS = {}
    countT = {}

    for i in range(len(s)):
        #this is the same as saying countS[s[i]] += 1
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    if countS == countT:
        return True
    return False


print(isAnagram("anagram", "nagaram"))