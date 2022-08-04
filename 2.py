# Definition for singly-linked list.

from copy import deepcopy

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        for_next = 0
        first = l1.val + l2.val
        if first >= 10:
            first = first % 10
            for_next = 1
        
        l1 = l1.next
        l2 = l2.next

        current_node = ListNode( val = first )

        if l1 == None and l2 == None:
            if for_next == 0:
                return current_node
            else:
                next_node = ListNode( val = for_next )
                current_node.next = next_node
                return current_node

        elif l1 == None and l2 != None:
            l1 = ListNode( val = 0)
        elif l1 != None and l2 == None:
            l2 = ListNode( val = 0)  

        

        head = None

        extra_case_flag = 0
        head_copy_flag = 1


        
        while True:
            current = l1.val + l2.val + for_next

            if current >= 10:
                current = current % 10
                for_next = 1
            else:
                for_next = 0    
            
            next_node = ListNode( val = current )
            current_node.next = next_node
            

            if head_copy_flag:
                head = deepcopy(current_node)
                head_copy_flag = 0

            current_node = next_node    

            l1 = l1.next
            l2 = l2.next

            if l1 == None and l2 == None:
                if for_next == 0:
                    break
                else:
                    extra_case_flag = 1

            elif l1 == None and l2 != None:
                l1 = ListNode( val = 0)
            elif l1 != None and l2 == None:
                l2 = ListNode( val = 0)    


            if extra_case_flag == 1:
                next_node = ListNode( val = for_next )
                current_node.next = next_node
                break

        return head




