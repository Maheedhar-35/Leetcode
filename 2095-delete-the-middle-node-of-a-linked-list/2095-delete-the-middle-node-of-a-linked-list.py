# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None
        curr=head
        c=[]
        while curr is not None:
            c.append(curr.val)
            curr=curr.next
        curr=head
        for i in range(len(c)//2):
            if i==len(c)//2-1:
                curr.next=curr.next.next
            curr=curr.next    
        return head    
