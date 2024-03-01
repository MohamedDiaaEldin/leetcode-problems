

'''
125. Valid Palindrome
Solved
Easy
Topics
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

'''
import re

def isPalindrome( s):
    """
    :type s: str
    :rtype: bool
    """
    ## convert to lowercase 
    s = s.lower() 
    ## replace non chars and number into empty string
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    left, right  = 0, len(s) - 1
    # time o(n/2) = o(n)
    # space o(1)
    while left < right : 
        if s[left] != s[right] : 
            return False
        left += 1 
        right -= 1
    return True



        
def isPalindrome_v2( s):
    ## convert to lowercase 
    s = s.lower()
    ## replace non chars and number into empty string
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    return s[::-1] == s



s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
print(isPalindrome_v2(s))

