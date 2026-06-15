# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        c=[]
        curr=head
        while curr is not None:
            c.append(curr.val)
            curr=curr.next
        curr=head
        c.sort()
        i=0
        while curr is not None:
            curr.val =c[i]
            curr=curr.next
            i+=1
        return head     