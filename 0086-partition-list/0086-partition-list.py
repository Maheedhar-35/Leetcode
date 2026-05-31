# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        result=ListNode()
        dummy =result
        curr=head
        count=[]
        while curr!=None:
            count.append(curr.val)
            curr=curr.next
        count1=[t for t in count if t < x]
        count2=[t for t in count if t>=x]
        while count2!=[]:
            count1.append(count2.pop(0))
        print(count1)
        i=0
        curr=head
        while curr!=None:
            curr.val=count1[i]
            curr=curr.next
            i+=1
        return head    