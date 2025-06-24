class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        first, second = 0, k
        sums = 0
        for i in range(k):
            sums += nums[i]
        
        maxSum = sums
        for i in range(k, len(nums)):
            sums -= nums[i-k]
            sums += nums[i]
            maxSum = max(sums, maxSum)

        return maxSum / k     
            