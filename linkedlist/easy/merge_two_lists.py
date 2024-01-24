
'''
21. Merge Two Sorted Lists
Easy
Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# creates new output linked list
def mergeTwoLists(self, list1, list2):
    head = ListNode()
    current = head
    while list1 and list2 : 
        if list1.val < list2.val: 
            current.next = list1 
            list1 = list1.next 
        else:
            current.next = list2 
            list2 = list2.next 
        current = current.next         
    current.next = list1 or list2
    return head.next




# merge it in place 
def mergeTwoLists_v2(self, list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    dummy_head = ListNode()
    dummy_head.next = list1  # Use dummy head to simplify handling the first node
    current = dummy_head
    while list1 and list2:
        if list1.val < list2.val:
            list1 = list1.next                
        else:
            temp = list2.next
            list2.next = current.next
            current.next = list2
            list2 = temp
        current = current.next

    current.next = list1 or list2

    return dummy_head.next
