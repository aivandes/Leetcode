class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = node = ListNode()
        
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                node.next = ListNode(list1.val)
                node = node.next
                list1 = list1.next
            
            else:
                node.next = ListNode(list2.val)
                node = node.next
                list2 = list2.next
            
        if list1 is not None:
                node.next = list1
        else:
            node.next = list2
                
        
        return head.next
