# Definition for singly-linked list.
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
        if first > 10:
            first = first % 10
            for_next = 1
        
        l1 = l1.next
        l2 = l2.next
        
        sum = ListNode( val = first )
        
        while True:
            current = l1.val + l2.val + for_next
            if current > 10:
                current = current % 10
                for_next = 1
            
            ListNode( val = current )






