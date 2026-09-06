class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set()
        for num in nums:
            st.add(num)
        max_num = 0
        for num in st:
            if (num-1) not in st:
                cnt = 1
                while (num+1) in st:
                    cnt += 1
                    num += 1
                max_num = max(max_num, cnt)
        return max_num