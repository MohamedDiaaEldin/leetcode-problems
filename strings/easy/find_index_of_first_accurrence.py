'''
28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.


'''
# O(n)
def strStr( haystack, needle) :
    if len(needle) > len(haystack):
        return -1

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1


#time O(N)
def strStr_v2( haystack, needle) :
    if len(needle) > len(haystack) : 
        return -1
    i = 0
    while i < len(haystack):
        if haystack[i] == needle[0]:                    
            match = True
            for j in range(1, len(needle)):                
                if i + j  == len(haystack) or  haystack[i + j] != needle[j] :
                    match = False
                    break                
            if match : 
                return i 
        i += 1
    return -1 


#time O(N)
def strStr_v3( haystack, needle) :
    if len(needle) > len(haystack) : 
        return -1
    i = 0
    while i < len(haystack):
        if haystack[i] == needle[0]:                    
            ii = i 
            for j in range(len(needle)):                
                if  ii < len(haystack) and  haystack[ii] == needle[j] :
                    if j == len(needle) -1: 
                        return i
                    ii += 1 
                else : 
                    break
        i += 1
    return -1 

def strStr_v4( haystack, needle) :
    try  : 
        return haystack.index(needle)
    except : 
        return -1

haystack = "mississippi"
needle = "issipi"

print(strStr_v2(haystack, needle))