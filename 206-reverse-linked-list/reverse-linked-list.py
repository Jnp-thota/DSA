# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        if  head is None:  # only one node
            return head
        fur = head.next
        while curr is not None and curr.next is not None:
           curr.next = prev
           prev = curr
           curr = fur
           fur = curr.next
        curr.next = prev
        return curr
        


        