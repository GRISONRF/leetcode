# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # creating a dummy linked list
        dummy = ListNode()
        output = dummy # setting the dummy LL to be the output result
        
        
        
        
        # iterate through boths lists to find the smallest and keep printing it until find node.next == none.
        while list1 and list2:   # while we have the 2 lists
            if list1.val < list2.val:   # if the head value of first list is smaller than head value of second list
                output.next = list1     # add the list1 (which is just the head of list1) in the output list as the next node
                list1 = list1.next      # setting the next node in list to be the head - so we can compare to the head of list2 in the loop.
            else:   # if list2.val is greater than list1.val
                output.next = list2     # add the head of list2 as output.next
                list2 = list2.next      # set the head of list2 to be the list2.next -so we can compare to the head of list1
            output = output.next # regardless of the condition, need to update the output -> in other words, add the 
                
         # If one of the lists is/get empty
        if list1 == None:
            output.next = list2
        
        if list2 == None:
            output.next = list1   
            
        return output
                
                # ************** NOT DONE **********