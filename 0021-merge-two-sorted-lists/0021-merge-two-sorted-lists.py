# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Create a dummy node to serve as the starting point of the merged list 
        dummy = ListNode()
        current = dummy 
        
        #Traverse both lists and add the smallest node to the merged list
        while list1 and list2: 
            if list1.val < list2.val:
                current.next = list1 
                list1 = list1.next
            else:
                current.next = list2 
                list2 = list2.next
            current = current.next
                
        #If one of the lists is not empty, append it to the merged list 
        if list1: 
            current.next = list1 
        else: 
            current.next = list2
            
        #The merged list starts from the next node of the dummy 
        return dummy.next
    
#Function to print the linked list for verification
def print_linked_list(head):
    current = head 
    while current: 
        print(current.val, end = " -> ")
        current = current.next
    print("None")