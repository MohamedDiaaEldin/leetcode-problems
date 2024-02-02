class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


last = ListNode(2, None)
second = ListNode(3, last)
first = ListNode(5, second)


cur = ListNode(None, first) 
cur.next.next = last
# while cur : 
#     print(cur.val)
#     cur = cur.next 


print('##')
while first : 
    print(first.val)
    first = first.next
