class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        l = 0
        h = (len(mat)*len(mat[0]))-1

        while l<=h:
            m = (l+h)//2
            r = m//len(mat[0])
            c = m%len(mat[0])
            if mat[r][c] == target:
                return True
            elif mat[r][c] > target:
                h = m-1
            else:
                l = m+1
        return False