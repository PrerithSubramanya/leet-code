'''Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.
Example 1:
Input: heights = [2,1,5,6,2,3] Output: 10 Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:
Input: heights = [2,4] Output: 4

Constraints:

1 <= heights.length <= 105 0 <= heights[i] <= 104'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                Area = stack[-1][1] * (i - stack[-1][0])
                start = stack[-1][0]
                maxArea = max(maxArea, Area)
                stack.pop()
            stack.append([start, h])

        for i in range(len(stack)):
            area = stack[i][1] * (len(heights) - stack[i][0])
            maxArea = max(maxArea, area)
        return maxArea