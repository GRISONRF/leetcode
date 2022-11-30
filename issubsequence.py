def isSubsequence(s, t):
    ans = []
    s1 = list(s)
    print(s1)

    for i in t[::-1]:
        if s1 and i == s1[-1]:
            ans.append(i)
            s1.pop()
    if ''.join(ans[::-1]) == s:
        return True
    return False
    
            
    
        
print(isSubsequence('b', 'abc')) #true
print(isSubsequence('axc', 'ahbgdc'))