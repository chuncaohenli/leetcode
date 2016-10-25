# Find out the pattern firt, new[j][n-i-1] = old[i][j]

class Solution(object):
    # It is not in-place solution
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        result = [[] for i in range(len(matrix))]
        for i in result:
            for j in range(n):
                i.append(0)
        
        for i in range(n):
            for j in range(n):
                result[j][n-1-i] = matrix[i][j]
                
        for i in range(n):
            for j in range(n):
                matrix[i][j] = result[i][j]
                
    # It is in-place Solution
    # rotate from outter circle to inner
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n-1):
            for j in range(i, n-1-i):
                x = i
                y = j

                tmp = matrix[x][y]
                for k in range(4):

                    replacedNum = matrix[y][n - x - 1]
                    matrix[y][n - x - 1] = tmp

                    tmp = replacedNum
                    x, y = y, n - x - 1
        
