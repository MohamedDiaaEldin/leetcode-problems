'''
86. Partition List
Solved
Medium
Topics
Companies
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200

'''
from LinkedList import ListNode, build_linked_list, print_linked_list

# time  o(n)
# space o(1)
def partition(head, x):
    left, right = ListNode(), ListNode()
    cur_left, cur_right = left, right
    cur = head 
    while cur : 
        if cur.val >= x : 
            cur_right.next = cur
            cur_right = cur_right.next
        else : 
            cur_left.next = cur                 
            cur_left = cur_left.next
        cur = cur.next 
    cur_right.next = None 
    cur_left.next = right.next
    return left.next


# this approach will work if we want all number greater to x to be after x and the less number before it 
# time  o(n)
# space o(1)
def partition_v2(head, x):
    i = 0 
    wanted = head 
    while wanted and wanted.val != x:
        wanted = wanted.next
        i += 1 
    ## i = 2
    ## wanted.val = 3 
    dummy = ListNode(None, head ) 
    prv , cur = dummy, dummy.next
    j = 0
    while cur : 
        if cur.val > x and j < i:                
            wanted_next = wanted.next
            cur_next = cur.next 
            wanted.next = cur 
            cur.next = wanted_next
            prv.next = cur_next
            prv = cur
            cur = cur_next
            i -= 1
        elif cur.val < x and j > i : 
            head_next = head.next
            cur_next = cur.next
            # 
            head.next = cur                 
            prv.next = cur.next
            cur.next = head_next
            cur = cur_next
            i += 1
        else : 
            prv = cur
            cur = cur.next
        j += 1 
    return head

head = build_linked_list([1,4,3,2,5,2]) 
new_head = partition(head, 3)
print_linked_list(new_head)
new_head = partition_v2(head, 3)
print_linked_list(new_head)

