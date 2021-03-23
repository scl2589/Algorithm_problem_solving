# Deque 활용

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = collections.deque() 
        
        if not head:
            return True
        
        node = head
        
        while node is not None:
            q.append(node.val)
            node = node.next 
        
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True
        

# List 활용
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        
        if not head:
            return False
    
        node = head
        
        while node is not None:
            arr.append(node.val)
            node = node.next
        
        if arr == arr[::-1]:
            return True
        else:
            return False