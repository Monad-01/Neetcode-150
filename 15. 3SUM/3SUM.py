class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        

        for fp in nums:
            lp=len(nums)
            if len(nums) == 3 and sum(nums) == 0:
                return [nums]
            while fp < (lp - 1):
                lastTriplet = (nums[fp] + nums[lp - 1]) * -1
                if lastTriplet in nums[fp:lp]:
                    solution = sorted([nums[fp],nums[lp-1],lastTriplet])
                    if solution not in output:
                        output.append(solution)
                lp -= 1

        return output




