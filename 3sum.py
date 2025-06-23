class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        pairs = []
        for i,v in enumerate(nums):
            first = i+1
            second = len(nums)-1
            while first < second:
                temp = v + nums[first] + nums[second]
                if temp < 0:
                    first += 1
                elif temp > 0:
                    second -= 1
                elif temp == 0:
                    pairs.append([v, nums[first], nums[second]])
                    first += 1
                    second -= 1
        newSet = set(tuple(p) for p in pairs)
        return list(newSet)