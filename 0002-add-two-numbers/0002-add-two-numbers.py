# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Create a dummy node to start the result linked list
        dummy = ListNode()
        current = dummy 
        carry = 0
        
        #Iterate through both lists until both are exhausted and there is no carry left
        while l1 or l2 or carry: 
            #Sum the values of the nodes (if they exist) and the carry
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry 
            carry = total // 10 
            current.next = ListNode(total % 10)
            
            #Move to the next nodes 
            current = current.next
            if l1:
                l1 = l1.next
            if l2: 
                l2 = l2.next
                
        return dummy.next
# Function to print the linked list for verification
def print_linked_list(head: Optional[ListNode]): 
    current = head
    while current: 
        print(current.val, end = " -> ")
        current = current.next
    print("None")