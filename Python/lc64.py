class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        mem = [grid[i][:] for i in range(len(grid))]
        
        for i in range(1,len(grid)):
            mem[i][0] = mem[i][0] +  mem[i-1][0]
        
        for i in range(1,len(grid[0])):
            mem[0][i] = mem[0][i] + mem[0][i-1]
            
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                mem[i][j] = mem[i][j] + min(mem[i-1][j],mem[i][j-1])
                
        return mem[-1][-1]
