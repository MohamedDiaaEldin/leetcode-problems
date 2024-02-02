# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """


    new_head = ListNode(None, head)
    prv, cur = new_head, head 
    while cur :
        if cur.val == val : 
            prv.next = cur.next 
        else: 
            prv = prv.next 
        cur = cur.next
    return new_head.next
def removeElements_v1(head, val):
    while head and head.val == val : 
        head = head.next     
    prv = ListNode(None, head)
    cur = head 
    while cur : 
        if cur.val == val : 
            prv.next = cur.next
        else: 
            prv = prv.next
        cur = cur.next
    return head
        
