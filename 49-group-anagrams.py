class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #creates a dict with a list as value
        letters_to_words = defaultdict(list)

        #iterate over the words in the list
        for word in strs:
            #sort the LETTERS in the word and add as a key (thats why we make into a tuple) and append the word itself to it.
            #since we used the defaultdict, it will only create a new key if these sorted letters are not already in the dict. if they are, will just add the letter as a value
            letters_to_words[tuple(sorted(word))].append(word)
        #return a list containing the values of the dictionary
        return list(letters_to_words.values())
       