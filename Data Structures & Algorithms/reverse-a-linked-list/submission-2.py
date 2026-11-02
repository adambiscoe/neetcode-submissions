# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        if head == None:
            return head
        while current.next != None:
            stack.append(current)
            current = current.next
        newhead = current
        while len(stack) != 0:
            current.next = stack.pop()
            current = current.next
        current.next = None
        return newhead

        