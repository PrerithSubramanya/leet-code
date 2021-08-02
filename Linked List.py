#!/usr/bin/env python
# coding: utf-8

# 206. Reverse Linked List
# Easy
# 
# 7707
# 
# 143
# 
# Add to List
# 
# Share
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# 
#  
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: [2,1]
# Example 3:
# 
# Input: head = []
# Output: []
#  
# 
# Constraints:
# 
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
#  
# 
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# In[1]:


class ListNode:
    def __init__(self, val =0, next = None):
        self.val = val
        self.next = None

class Solution: 
    def reverseList(self, head:ListNode) -> ListNode: # iterative method
        cur = head
        prev = None
        next_node = head
        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev
    def reverseList_recursive(self, head:ListNode) -> ListNode: #recursive method
        return 


# 23. Merge k Sorted Lists
# Hard
# 
# 8041
# 
# 372
# 
# Add to List
# 
# Share
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# 
# Merge all the linked-lists into one sorted linked-list and return it.
# 
#  
# 
# Example 1:
# 
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:
# 
# Input: lists = []
# Output: []
# Example 3:
# 
# Input: lists = [[]]
# Output: []
#  
# 
# Constraints:
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.

# In[3]:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap_ele = []
        for i, row in enumerate(lists):
            if row:
                heappush(heap_ele, (row.val, i))
        dummy = cur = ListNode()    
        while heap_ele:
            val, index = heappop(heap_ele)
            cur.next = ListNode(val)
            if lists[index].next:
                lists[index] = lists[index].next
                heappush(heap_ele, (lists[index].val, index))
            cur = cur.next
        return dummy.next


# 141. Linked List Cycle
# Easy
# 
# 5074
# 
# 643
# 
# Add to List
# 
# Share
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# 
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# 
# Return true if there is a cycle in the linked list. Otherwise, return false.
# 
#  
# 
# Example 1:
# 
# 
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:
# 
# 
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:
# 
# 
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#  
# 
# Constraints:
# 
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
#  
# 
# Follow up: Can you solve it using O(1) (i.e. constant) memory?

# In[4]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pointer1 = head
        pointer2 = head
        
        while pointer1 and pointer2 and pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            if pointer1 == pointer2:
                return True
        return False


# 21. Merge Two Sorted Lists
# Easy
# 
# 7656
# 
# 827
# 
# Add to List
# 
# Share
# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
# 
#  
# 
# Example 1:
# 
# 
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
# 
# Input: l1 = [], l2 = []
# Output: []
# Example 3:
# 
# Input: l1 = [], l2 = [0]
# Output: [0]
#  
# 
# Constraints:
# 
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.

# In[5]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = dummy = ListNode()
        if not l1 and not l2:
            return None
        elif l1 and not l2:
            return l1
        elif l2 and not l1:
            return l2
        else:
            while l1 and l2:
                if l1.val < l2.val:
                    output.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    output.next = ListNode(l2.val)
                    l2 = l2.next
                output = output.next
            if l1:
                output.next = l1
            if l2:
                output.next = l2
        return dummy.next


# 19. Remove Nth Node From End of List
# Medium
# 
# 6189
# 
# 339
# 
# Add to List
# 
# Share
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# 
#  
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
# 
# Input: head = [1], n = 1
# Output: []
# Example 3:
# 
# Input: head = [1,2], n = 1
# Output: [1]
#  
# 
# Constraints:
# 
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#  
# 
# Follow up: Could you do this in one pass?

# In[3]:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        
        for i in range(n):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


# 143. Reorder List
# Medium
# 
# 3586
# 
# 157
# 
# Add to List
# 
# Share
# You are given the head of a singly linked-list. The list can be represented as:
# 
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# 
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# 
#  
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#  
# 
# Constraints:
# 
# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000

# In[4]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        
        dummy = head
        curr = head
        #find the middle of the node
        while curr.next and curr.next.next:
            dummy = dummy.next
            curr = curr.next.next
        split = dummy.next
        dummy.next = None
        #reverse the second half of the node
        prev = None
        next_node  = None
        while split:
            next_node = split.next
            split.next = prev
            prev = split
            split = next_node
            
        # iterate and concatenate alternate elements from both the lists    
        point1 = head
        point2 = prev
        temp = None
        while point2:
            temp = point1.next
            point1.next = point2
            point1 = point2
            point2 = temp


# In[ ]:




