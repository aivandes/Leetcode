    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        node = head.next
        previous = head
        while node:
            
            if node.val == previous.val:
                previous.next = node.next
                node = node.next
            
            else:
                previous = node
                node = node.next
        
        return head
