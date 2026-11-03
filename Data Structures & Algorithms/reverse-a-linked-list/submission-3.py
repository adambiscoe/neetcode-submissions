# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = head
        curr = head
        nxt =  head.next
        head.next = None
        while nxt:
            curr = nxt
            nxt = curr.next
            curr.next = prev
            prev = curr
        return curr

        