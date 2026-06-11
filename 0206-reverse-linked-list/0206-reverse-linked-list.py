# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr=head
        c=[]
        while curr is not None:
            c.append(curr.val)
            curr=curr.next
        c=c[::-1]
        i=0
        curr=head
        while curr is not None:
            curr.val=c[i] 
            curr=curr.next
            i+=1
        return head    