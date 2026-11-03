# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and head.next and head.next.next:

            fast = head
            slow = head

            while fast.next:
                fast = fast.next
                if fast.next:
                    slow = slow.next
                    fast = fast.next
            
            

            prev = slow.next
            curr = slow.next
            nxt =  slow.next.next
            slow.next.next = None
            slow.next = None
            while nxt:
                curr = nxt
                nxt = curr.next
                curr.next = prev
                prev = curr
            firstHalf = head
            secondHalf = curr

            
            while secondHalf:
                fnext = firstHalf.next
                firstHalf.next = secondHalf
                sNext = secondHalf.next
                secondHalf.next = fnext
                secondHalf = sNext
                firstHalf = fnext
        
    




        