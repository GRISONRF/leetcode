"""
You are running a classroom and suspect that some of your students are passing around the answer to a multiple-choice question disguised as a random string.

Your task is to write a function that, given a list of words and a string, finds and returns the word in the list that is scrambled inside the string, if any exists. If none exist, it returns the result "-" as a string. There will be at most one matching word. The letters don't need to be in order or next to each other. The letters cannot be reused.

Example:  
words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax"]
string1 = "ctay"
find(words, string1) => "cat"   (the letters do not have to be in order)  
  
string2 = "bcanihjsrrrferet"
find(words, string2) => "cat"   (the letters do not have to be together)  
  
string3 = "tbaykkjlga"
find(words, string3) => "-"     (the letters cannot be reused)  
  
string4 = "bbbblkkjbaby"
find(words, string4) => "baby"    
  
string5 = "dad"
find(words, string5) => "-"    
  
string6 = "breadmaking"
find(words, string6) => "bird"    

All Test Cases:
find(words, string1) -> "cat"
find(words, string2) -> "cat"
find(words, string3) -> "-"
find(words, string4) -> "baby"
find(words, string5) -> "-"
find(words, string6) -> "bird"
  
Complexity analysis variables:  
  
W = number of words in `words`  
S = maximal length of each word or string  
"""


# from nis import match


# words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax"]
# string1 = "ctay"
# string2 = "bcanihjsrrrferet"
# string3 = "tbaykkjlga"
# string4 = "bbbblkkjbaby"
# string5 = "dad"
# string6 = "breadmaking"


# check if string had all the letters of word
# word1 -> each letter -> if this letter in string -> pop letter and store letter in a var ->  check if var == word.

def check_words(words, string):
    
    # #check if string not letter
    
    # for word in words:   # "baby"
    #     matched_letters = ""   #'b a b y'
    #     test_string = string
    #     for i, n in enumerate(word):   #'b'      
    #         if n in test_string:  # 'tbaykkjlga'              
    #             matched_letters += n               
    #             copy = test_string.replace(n,'-')
    #             print(copy)
    #     if matched_letters == word:
    #         return matched_letters

    # create empty dict to store letters from scramble string 
    letters = {}
    # populate dict with letters of string
    for char in string:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    # ctaay
    # letters = {c:1, t:1, a:2, y:1}
    print(letters)

    # check if letter in words is in the dict.
    # if its not, return '-'
    # if it is, i want to:
    # take 1 from the value of this letter in the dict.
    # add the word to the 

    match = ""
    ans = []

    for word in words:
        for char in word:
            print(char)
            print(letters)
            if char not in letters:
                return '-'









    #         else:

    #             if char in letters:
    #                 match += char
    #                 if(letters[char]) > 1:
    #                     letters[char] -= 1
    #                 elif letters[char] == 1:
    #                     letters.pop(char, 0)
    #                     continue
    #             if match == word:
    #                 ans.append(match)
    #                 return ans

    # return []



                # if letters[char] > 0:
                #     match += char
                #     letters[char] -= 1                 
                #     if match == word:
                #         return match

                
           
        

        


    # if I find a letter that is in the dict, 
                
                
    
    
    
    
print(check_words(["baby", "referee", "cat", "dada", "dog", "bird", "ax"],"tbaykkjlga"))