class Solution:
    def maxArea(self, heights: List[int]) -> int:
        high = 0
        first, second = 0, len(heights)-1
        while first != second:
            contain = (second - first) * min(heights[first], heights[second])
            high = max(high, contain)
            if heights[first] < heights[second]:
                first += 1
            else:
                second -= 1
        return high
        