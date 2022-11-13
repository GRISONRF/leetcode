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
        # setting the output result  to be the dummy LL
        output = dummy
        
        # iterate through boths lists to find the smallest and keep printing it until find node.next == none.
        # while we have the 2 lists
        # if the head value of first list is smaller than head value of second list
        # setting head of list1 to be the next node of otput. 
        # setting the next node in list to be the head - so we can compare to the head of list2 in the loop.
        # if list2.val is greater than list1.val
        # add the head of list2 as output.next
        # set the head of list2 to be the list2.next -so we can compare to the head of list1
        # regardless if the condition was met, need to update the output by saying the output is = to next output
        # If one of the lists is/get empty
        #update all the rest of output with the list that is not empty

        while list1 and list2:
            if list1 < list2:
                output.next = list1
                list1 = list1.next
            else:
                output.next = list2
                list2 = list2.next
            output = output.next

        if list1:
            output.next = list1
        if list2:
            output.next = list2
        
        return dummy.next