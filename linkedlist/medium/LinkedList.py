# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def build_linked_list(nums):
    dummy_head = ListNode()
    current = dummy_head
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy_head.next
def print_linked_list(head) : 
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print()
