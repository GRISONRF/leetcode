class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #list of strings
        #find the longest common prefix
        #if no common prefix return ""

        ans = ""
        #iterate over the range of len of first string
        for i in range(len(strs[0])):
            #iterate over every string
            for s in strs:
                #check if its on bounds=if the string at i is less than len of string + check if the string at i is same as string[0] at i. if not return ans
                if i >= len(s) or s[i] != strs[0][i]:
                    return ans
            ans+=s[i]
        
        return ans
