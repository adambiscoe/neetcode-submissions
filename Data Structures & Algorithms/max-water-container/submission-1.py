class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = 0
        beg = 0
        end = len(heights) - 1
        while beg < end:
            currArea = (end - beg) * min(heights[end], heights[beg])
            currMax = max(currArea, currMax)
            if heights[end] < heights[beg]:
                end -= 1
            else:
                beg += 1

        return currMax

        