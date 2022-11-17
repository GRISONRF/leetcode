
def longestPalindrome(s):

    
    """ just need to check how many pairs of the same letter we have, + 1 odd letter (for the center) 
    than return the length of it!! 

        "abccccdd"

    """

    map = {}
    # a:1, b:3, c:4, d:2
    res = 0
    odd = 0

    for char in s:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1
    print(map)

    for v in map.values():
        if v % 2 == 0:
            res += v
        else:
            odd += 1
            res += v

    if odd <= 1:
        return res
    return res - odd + 1


print(longestPalindrome("abccccdd"))
print(longestPalindrome("abcbe"))
print(longestPalindrome("ccc"))
