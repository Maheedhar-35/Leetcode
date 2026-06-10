# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None :
            return head
        curr = head
        i=1
        while curr.next is not None :
            if i%2==0:
                i+=1
                curr=curr.next
                continue
            temp=curr.val
            curr.val=curr.next.val
            curr.next.val=temp
            i+=1
            curr=curr.next
        return head        