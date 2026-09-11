class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = j = k = 0
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                tot = nums[i]+nums[j]+nums[k]
                if tot > 0:
                    k -= 1
                elif tot < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j<k and nums[j] == nums[j-1]: 
                        j += 1
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1
        return res 