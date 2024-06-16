"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
"""
"""
Trick : Iterate and reverse each k node set
"""
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:        
        curr = head
        # The left out nodes after k times will hit here
        for _ in range(k):
            if not curr: return head
            curr = curr.next

        # Reverse linked list
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Attach next set to current
        head.next = self.reverseKGroup(curr, k)
     
        return prev
