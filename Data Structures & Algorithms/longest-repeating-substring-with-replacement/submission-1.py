class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash = [0] * 26
        l = 0
        r = 0
        maxFreq = 0
        max_len = -1
        while (r<len(s)):
            hash[ord(s[r]) - ord('A')] += 1
            maxFreq = max(maxFreq, hash[ord(s[r]) - ord('A')])
            while (r-l+1-maxFreq>k and l<len(s)):
                hash[ord(s[l]) - ord('A')] -= 1
                for i in range(len(hash)):
                    maxFreq = max(maxFreq, hash[i])
                l += 1
            if (r-l+1-maxFreq <=k) :
                max_len = max(max_len, r-l+1)
            r += 1
        return max_len