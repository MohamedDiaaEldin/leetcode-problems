'''
876. Middle of the Linked List
Solved
Easy
Topics
Companies
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(n) + O(n)
def middleNode( head):
    cur = head 
    count = 1
    while cur : 
        cur = cur.next 
        count += 1 
    cur = head        
    mid = count // 2 + 1        
    while mid < count and cur.next:            
        cur = cur.next
        mid += 1
    return cur

def middleNode_v1( head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # 1
    # 1 2
    # 1 2 3 
    # 1 2 3 4
    # 1 2 3 4 5
    slow, fast = head, head
    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
    return slow
    
    