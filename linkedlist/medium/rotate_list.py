'''
61. Rotate List
Solved
Medium
Topics
Companies
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head or (head and not head.next): 
        return head
    left, tail = head, head         
    length = 1
    while tail.next : 
        tail = tail.next
        length += 1
    k = k % length
    if k == 0 : 
        return head
    for i in range(length - k -1):
        left = left.next
    new_head = left.next
    tail.next = head 
    left.next = None    

    return new_head
