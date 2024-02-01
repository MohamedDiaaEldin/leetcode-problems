# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## O(n) Time
## O(1) Space
def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head.next :
        return True
    slow, fast = head , head
    # reach to the middle and last
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    ## reverse 
    prv = None 
    while slow : 
        next = slow.next 
        slow.next = prv 
        prv = slow 
        slow = next
    while prv : 
        if head.val != prv.val : 
            return False
        head = head.next 
        prv = prv.next
    return True

# O(n) Time
# O(n) Space
def isPalindrome_v2(head):
    ###
    ar = []
    cur = head 
    while cur : 
        ar.append(cur.val)
        cur = cur.next
    left, right = 0, len(ar) - 1
    while left < right: 
        if ar[left] != ar[right]: 
            return False
        left += 1 
        right -= 1

    return True