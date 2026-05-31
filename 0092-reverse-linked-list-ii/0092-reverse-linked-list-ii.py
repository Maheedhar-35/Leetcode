# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        result=ListNode()
        dummy=result
        curr=head
        count=[]
        while curr!=None:
            count.append(curr.val)
            curr=curr.next
        count[left-1:right]=count[left-1:right][::-1]    
        print(count)
        curr=head
        i=0
        while curr!=None:
            curr.val=count[i]
            curr=curr.next
            i+=1
        return head    