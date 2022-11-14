# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        
        stack = []
        temp = head
        
        while temp:
            stack.append(temp)
            temp = temp.next
        
        temp = head
        while True:
            if len(stack) and temp == stack[-1]:
                temp.next = None
                break
            elif len(stack) and temp.next == stack[-1]:
                nxtnode = stack.pop()
                nxtnode.next = None
                break
                
            nxtnode = temp.next
            first = temp
            sec = stack.pop()
            first.next = sec
            sec.next = nxtnode
            temp = nxtnode
        
        
            
        