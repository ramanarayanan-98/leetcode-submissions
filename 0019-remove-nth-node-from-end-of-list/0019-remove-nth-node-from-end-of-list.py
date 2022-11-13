# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        fast = head
        count = 0
        
        while fast and count < n-1:
            fast = fast.next
            count += 1
        
        if count != n-1:
            return head
        prev = None
        slow = head
        while fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        if not prev:
            return head.next
        prev.next = slow.next
        
        return head