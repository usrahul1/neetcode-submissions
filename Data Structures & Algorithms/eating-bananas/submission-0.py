class Solution:
    def f(self, piles, r):
        ans = 0
        for i in range(len(piles)):
            ans += math.ceil(piles[i]/r)
        return ans
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l<=r: 
            mid = (l+r)//2
            num = self.f(piles, mid)
            if num<=h:
                r = mid-1
            else:
                l = mid+1
        return l