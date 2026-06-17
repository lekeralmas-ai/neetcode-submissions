# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        cNode1 = list1
        cNode2 = list2
        l1 = list()
        l2 = list()
        while cNode1:
            l1.append(cNode1.val)
            cNode1 = cNode1.next
        while cNode2:
            l2.append(cNode2.val)
            cNode2 = cNode2.next
        l_m = sorted(l1 + l2)
        dummy = ListNode()
        cNode = dummy
        for v in l_m:
            cNode.next = ListNode(v)
            cNode = cNode.next
        return dummy.next