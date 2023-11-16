class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        L = 0
        minLength = float('inf')
        curSum = 0

        for R in range(len(nums)):
            curSum += nums[R]

            while curSum >= target:
                minLength = min(R - L + 1, minLength)
                curSum -= nums[L]
                L += 1
    
        if minLength == float('inf'):
            return 0
        
        return minLength
            
        