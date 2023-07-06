class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        suff = [0] * len(nums)

        pre[0] = 1
        suff[len(nums) - 1] = 1

        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        
        for n in range(len(nums) - 1, 0, -1):
            suff[n-1] = suff[n] * nums[n]

        ans = []
        for i in range(len(nums)):
            ans.append(pre[i] * suff[i])
        
        return ans
