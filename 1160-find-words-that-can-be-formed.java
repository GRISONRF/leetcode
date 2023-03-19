public class 1160-find-words-that-can-be-formed {
    class Solution {
        public int countCharacters(String[] words, String chars) {
            
            String ans = "";
    
            //iterate over words
            for (String word : words) {
    
                //initialize a map for chars
                Map<Character, Integer> charMap = new HashMap<>();
                //create the map with char and its frequencies
                for (var c : chars.toCharArray()){
                    charMap.put(c, charMap.getOrDefault(c, 0) + 1);
                }
    
                //iterate over word
                for (int i=0; i<word.length(); i++){
                    //if word is not in chars map or the value for this char is less than 1
                    if (!charMap.containsKey(word.charAt(i)) || charMap.get(word.charAt(i)) < 1) {break;}
                    //if word is in map and the value is more or equal to 1
                    if (charMap.containsKey(word.charAt(i)) && charMap.get(word.charAt(i)) >= 1){
                        //delete 1 to the value of this char
                        charMap.put(word.charAt(i), charMap.get(word.charAt(i)) - 1);
                        //if this is the last iteration (last letter of this word)
                        if (i == word.length() -1 ){ 
                            ans += word; 
                        }
                    }
                }
            }
            //return len on answer
            return ans.length();
        }
    }
}
