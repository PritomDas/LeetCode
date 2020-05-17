#this video reference was super helpful
[https://www.youtube.com/watch?v=zeR8iXo0JRM&feature=youtu.be]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        #dummy node and the current pointer
        dummy = curr = ListNode(0)
        while l1 or l2:
            #if both the lists are present and non empty
            if l1 and l2:
                if l1.val<l2.val:
                    curr.next =l1
                    l1 = l1.next
                    curr = curr.next
                else:
                    curr.next =l2
                    l2 = l2.next
                    curr = curr.next
            #if only one of the list is present, the other one may have reached null or absent
            #elif l1 or l2:
            else:
                curr.next = l1 if l1 else l2
                break;
        return dummy.next
