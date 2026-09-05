class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size = len(nums)
        nums = set(nums)
        return False if len(nums) == size else True