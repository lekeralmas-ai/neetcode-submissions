# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cnode1 = head
        cnode2 = head
        while cnode2 and cnode2.next:
            cnode1 = cnode1.next
            cnode2 = cnode2.next.next
            if cnode1 == cnode2:
                return True
        return False