""" 
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

A Container is an object that is used to store different objects and provide a way to access the contained objects and iterate over them.

from collections import Counter 
    
# With sequence of items  
print(Counter(['B','B','A','B','C','A','B',
               'B','A','C']))
    
# with dictionary 
print(Counter({'A':3, 'B':5, 'C':2}))

or collections.Counter()

 """

class Solution:
    def firstUniqChar(self, s: str) -> int:
        #leetcode


        #to store letters and how many times it appears
        count = {}   #l:1, e:2

        #iterate through the string and add each letter to the dict
        for letter in s:
            if letter not in count:    #le
                count[letter] = 1
            else:
                count[letter] += 1
        
        for k, v in count.items():
            if v == 1:
                return s.index(k)
            
        return -1


###SOLUTION 2, USING COLLECTIONS

import collections
def firstUniqChar(s):
    #leetcode


    #to store letters and how many times it appears
    count = collections.Counter(s)
    print(count)
    
    for idx, char in enumerate(s):
        if count[char] == 1:
            return idx

    return -1
   
        
print(firstUniqChar('loveleetcode'))