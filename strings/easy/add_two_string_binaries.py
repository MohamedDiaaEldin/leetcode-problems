'''

67. Add Binary
Solved
Easy
Topics
Companies
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

''' 
    1
    ^ 
   1010
   1011
   -----
   10101
0 + 0 = 0
0 + 1 = 1
1 + 1 = 0 (carry=1)
 
'''
# o(n)
def addBinary(a, b):
    # Initialize variables for the result and carry
    result = ''
    carry = 0
    
    # Start from the rightmost bit and iterate towards the leftmost bit
    i = len(a) - 1
    j = len(b) - 1
    
    while i >= 0 or j >= 0 or carry:
        # Calculate the sum of the current bits and the carry
        sum_bits = carry
        
        if i >= 0:
            sum_bits += int(a[i])
            i -= 1
        if j >= 0:
            sum_bits += int(b[j])
            j -= 1
        
        # Update the result and carry
        result = str(sum_bits % 2) + result
        carry = sum_bits // 2
    
    return result

def addBinary_v2(a,b):     
    return bin(int(a,2)+int(b,2))[2:]

def addBinary_v3(a, b): 
    x, y = int(a, 2), int(b, 2)    
    while y:
        answer = x ^ y ## bit addition
        carry = (x & y) << 1 
        x, y = answer, carry
    return bin(x)[2:]
a = "11"
b = "1"

print(addBinary(a,b ))
print(addBinary_v2(a,b ))
print(addBinary_v3(a,b ))