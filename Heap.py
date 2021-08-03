#!/usr/bin/env python
# coding: utf-8

# 23. Merge k Sorted Lists
# Hard
# 
# 8095
# 
# 374
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
# The sum of lists[i].length won't exceed 10^4

# In[2]:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # basic checks 
        if len(lists) == 1:
            return lists[0]
        elif len(lists) < 1:
            return None
        
        # insert head node values with list index 
        else:
            heap = []
            for i, list_ele in enumerate(lists):
                if list_ele:
                    heappush(heap, (list_ele.val, i))
            
            
            dummy = merge = ListNode(0)
            #now heap pop each element to form a new sorted merged list
            while heap:
                val, index = heappop(heap)
                merge.next = ListNode(val)
                if lists[index].next:
                    heappush(heap, (lists[index].next.val, index))
                    lists[index] = lists[index].next
                merge = merge.next
            return dummy.next


# 347. Top K Frequent Elements
# Medium
# 
# 5662
# 
# 284
# 
# Add to List
# 
# Share
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# 
#  
# 
# Example 1:
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# 
# Input: nums = [1], k = 1
# Output: [1]
#  
# 
# Constraints:
# 
# 1 <= nums.length <= 105
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#  
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# In[3]:


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] +=1
        heap = []
        output = []
        for key, val in hash_map.items():
            heappush(heap, (-val, key))
        for i in range(k):
            val, key = heappop(heap)
            output.append(key)
        return output
            


# 295. Find Median from Data Stream
# Hard
# 
# 4962
# 
# 88
# 
# Add to List
# 
# Share
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.
# 
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
# 
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
#  
# 
# Example 1:
# 
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
# 
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
#  
# 
# Constraints:
# 
# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.
#  
# 
# Follow up:
# 
# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

# In[4]:


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num)
        heappush(self.min_heap, -heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) != len(self.max_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0]-self.max_heap[0])/2


# In[ ]:




