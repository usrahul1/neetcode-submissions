class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        res = []
        while l<r:
            tot = nums[l]+nums[r]
            if tot > target:
                r -= 1
            elif tot < target:
                l += 1
            else:
                res.append(l+1)
                res.append(r+1)
                break
        return res