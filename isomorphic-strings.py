def isIsomorphic(s, t):

        """ 
        egg => add
        egg != dog
        
        create a dict for s
        create a dict for t
        """

        map_s_t = {}
        map_t_s = {}

        for cs, ct in zip(s, t):
                

            if cs not in map_s_t and ct not in map_t_s:
                map_s_t[cs] = ct
                map_t_s[ct] = cs

            elif map_s_t.get(cs) != ct or map_t_s.get(ct) != cs:
                return False
        return True
                 
                


        

     

print(isIsomorphic("badc", "baba"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("aaeaa", "uuxyy"))
