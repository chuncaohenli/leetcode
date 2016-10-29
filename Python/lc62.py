#
class Solution(object):
    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        
        mem = [[] for i in range(m+1)]
        for tmp in mem:
            for i in range(n+1):
                tmp.append(0)
        
        for i in range(m+1):
            mem[i][1] = 1
        for i in range(n+1):
            mem[1][i] = 1
        
        for i in range(2,m+1):
            for j in range(2,n+1):
                mem[i][j] = mem[i-1][j] + mem[i][j-1]
        
        return mem[m][n]
