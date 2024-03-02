'''
168. Excel Sheet Column Title
Solved
Easy
Topics
Companies
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

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

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 231 - 1


'''


def convertToTitle( columnNumber):
    """
    :type columnNumber: int
    :rtype: str
    """
    '''
    if input is 26
    columnNumber -= 1 # 25
    reminder = 25 % 26 # 25
    title = char(25 + 65 ) # Z
    ###
    if input is 28
    # first loop
    columnNumber -= 1 # 27
    reminder = 27 % 26 # 1
    title = char(1 + 65 ) # B

    # second loop 
        columnNumber -= 1 # 0
        reminder = 0 % 26 # 1
        title = char(0 + 65 ) # A
    '''
    title = ""
    while columnNumber > 0:
        # Subtract 1 to convert to 0-based indexing
        columnNumber -= 1
        # Get the remainder when divided by 26
        remainder = columnNumber % 26
        # Convert the remainder to the corresponding uppercase letter
        title = chr(remainder + ord('A')) + title
        # Divide columnNumber by 26 to move to the next position
        columnNumber //= 26
    return title


## I need to come back to that 
def convertToTitle_v2(columnNumber):
    output = ""
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while columnNumber:
        r = columnNumber % 26
        output = s[r-1] + output
    
        columnNumber = columnNumber // 26
        if r == 0:
            columnNumber -= 1
    return output


print(convertToTitle(28))
print(convertToTitle_v2(28))