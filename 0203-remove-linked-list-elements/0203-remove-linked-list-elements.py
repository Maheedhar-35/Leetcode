# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        result=ListNode()
        dummy=result
        curr=head
        while curr is not None:
            if curr.val==val:
                curr=curr.next
                continue
            dummy.next=ListNode(curr.val)
            dummy=dummy.next
            curr=curr.next
        return result.next