# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## enhancement of the first version 
## time o(n)
## space o(1)
def deleteDuplicates(head):

    if not head : 
        return None
    dummy = ListNode(None, head)
    prv = dummy
    cur = head 
    while cur : 
        if cur.next and cur.val == cur.next.val : 
            while cur.next and cur.val == cur.next.val : 
                cur = cur.next 
            prv.next = cur.next 
        else : 
            prv = prv.next 
        cur = cur.next

    return dummy.next

# first version
def deleteDuplicates_v1(head):
    if not head: 
        return None
    if head and head.next and not head.next.next:
        if head.val == head.next.val : 
            return None 
        else : 
            return head
    left, right = ListNode(None, head), head.next
    while right : 
        if left.next.val != right.val : 
            print('if -> left.next.val:',left.next.val , ' right.val :', right.val)
            right = right.next 
            left = left.next                 
        else : 
            print('else : left.next.val:',left.next.val , ' right.val :', right.val)
            while right and left.next.val == right.val : 
                right = right.next 
            if left.next == head :
                
                head = right
                left.next = head
            else : 
                left.next = right
            right  = right.next if right else None
    return head 

        