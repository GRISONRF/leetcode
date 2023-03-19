class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        #string good if can be formed using letters from char (only one)
        #check if each word uses ONLY words from char
        #add words into a var and return len of var

        result = ""

        # map chars = { l: frequency }
        chars_map = {}
        for c in chars:
            chars_map[c] = chars_map.get(c, 0) + 1
        # print(chars_map)
        
        #iterate words
        for word in words:
            #for each word, map letteres and frequency
            word_map = {}
           
            for c in word:
                word_map[c] = word_map.get(c, 0) + 1
            # print(word_map)
            
            temp_word = word
            for k, v in word_map.items():

                if k not in chars_map or v > chars_map[k]:
                    temp_word = ""
                    break
            result+=temp_word
        #return len of result
        return len(result)