class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i in range(len(nums)):
            if target - nums[i] in arr:
                return [arr[target - nums[i]], i]
            else:
                arr[nums[i]] = i
            