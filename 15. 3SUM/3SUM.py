class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        

        for fp in nums:
            lp=len(nums)
            while fp < lp - 1:
                lastTriplet = (nums[fp] + nums[lp - 1]) * -1
                if lastTriplet in nums[fp:lp]:
                    output.append(sorted([nums[fp],nums[lp],lastTriplet]))
                lp -= 1
        print(output)
        output = set(output)

        return output


