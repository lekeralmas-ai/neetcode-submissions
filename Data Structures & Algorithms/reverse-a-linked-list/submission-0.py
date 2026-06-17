# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        currentNode = head
        l = list()
        while currentNode:
            l.append(currentNode.val)
            currentNode = currentNode.next
        l2 = [0]*len(l)
        for i in range(len(l)):
            l2[i] = l[len(l)-1-i]
        currentNode= head
        t = 0
        while t < len(l2):
            currentNode.val = l2[t]
            currentNode= currentNode.next
            t +=1
        return head