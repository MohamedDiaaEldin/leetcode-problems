'''

171. Excel Sheet Column Number
Solved
Easy
Topics
Companies
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
'''


def titleToNumber(columnTitle):
    """
    :type columnTitle: str
    :rtype: int
    """
    multiplier = 1 
    column = 0
    for i in range(len(columnTitle) - 1, -1 , -1) :         
        column += (ord(columnTitle[i]) - 64) * multiplier ## 64 to map the ASCII values of uppercase letters to their corresponding value in the range 1 to 26 
        multiplier *= 26 
    return column


print(titleToNumber('AB'))