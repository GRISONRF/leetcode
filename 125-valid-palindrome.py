class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        
        salpha = ''.join(ch for ch in s if ch.isalnum())
        
        start = 0
        end = len(salpha)-1

        while start <= end:
            if salpha[start] != salpha[end]:
                False
            start+=1
            end-=1
        return True