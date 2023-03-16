class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #return sorted(s) == sorted(t)  #T:nlogn / M: n

        #not using sorting -T:O(n) M:O(n)
        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 0
            s_dict[s[i]] += 1

            if t[i] not in t_dict:
                t_dict[t[i]] = 0
            t_dict[t[i]] += 1

        return s_dict == t_dict
