'''
1290. Convert Binary Number in a Linked List to Integer
Solved
Easy
Topics
Companies
Hint
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
 

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue( head):
    """
    :type head: ListNode
    :rtype: int
    """
    current = head 
    binary = ''
    while current : 
        binary += str(current.val)
        current = current.next
    return int(binary, 2)


'''
Working with the solution
input 1011
Starting with an initial result of 0.
First bit (1): 0 * 2 + 1 = 1
Second bit (0): 1 * 2 + 0 = 2
Third bit (1): 2 * 2 + 1 = 5
Fourth bit (1): 5 * 2 + 1 = 11

'''
def getDecimalValue_v2(head):
    current  = head 
    result = 0
    while current : 
        result = result * 2 + current.val
        current = current.next
    return result