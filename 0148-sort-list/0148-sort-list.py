# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        current=head
        count=[]
        if head ==None:
            return head
        while current!=None:
            count.append(current.val)
            current=current.next 
        count=sorted(count)
        print(count)
        result=ListNode()
        dummy=result
        for i in range(len(count)):
            dummy.next=ListNode(count[i])
            dummy=dummy.next
        dummy.next=None    
        return result.next

        