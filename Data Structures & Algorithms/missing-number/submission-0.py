class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        res2 = 0
        n = len(nums)
        for i in range(n):
            res = res^i
            if(nums[i]>n):
                continue
            res2 = res2^nums[i]
        res = res^n
        return res^res2            