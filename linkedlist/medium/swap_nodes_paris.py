'''
24. Swap Nodes in Pairs
Solved
Medium
Topics
Companies
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    # if empty linkedlist or linkedlist length == 1
    if not head or (head and not head.next) : 
        return head
    left, right = head, head.next
    while right: 
        # swap values
        left_value = left.val
        left.val = right.val 
        right.val = left_value 
        ## update pointers
        left = right.next 
        right = right.next.next if right.next else None
    return head
        

