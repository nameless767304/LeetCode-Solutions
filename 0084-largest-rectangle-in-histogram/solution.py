class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        area = 0

        for idx, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                mid = stack.pop()
                left = stack[-1] if stack else -1
                area = max(heights[mid] * (idx - left - 1), area)
            
            stack.append(idx)
        return max(area, max(heights))

            


