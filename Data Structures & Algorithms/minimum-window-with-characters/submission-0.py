class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (s=="") or (t==""):
            return ""
        hash = [0]*256
        for i in range(len(t)):
            hash[ord(t[i])] += 1
        r = 0
        cnt = 0
        m = len(t)
        n = len(s)
        l = 0
        s_ind = -1
        max_len = 10e9
        while r<n:
            if hash[ord(s[r])] > 0:
                cnt += 1
            hash[ord(s[r])] -= 1
            while cnt == m:
                if (r-l+1)<max_len:
                    s_ind = l
                    max_len = r-l+1
                hash[ord(s[l])] += 1
                if hash[ord(s[l])] > 0 :
                    cnt -= 1
                l += 1
            r += 1
        if s_ind == -1:
            return ""
        return s[s_ind:s_ind+max_len]

            