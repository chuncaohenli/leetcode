# DP
# Consider the problem in this way
# P[i] denotes the max num of BST for array[1,2....i]
# P[i] = Sigma (R[j])
# R[j] denotes all BSTs rooted in node j
# R[j] = Sigma (P[i-1]*P[n-i+1])
#

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = [0 for i in range(n+1)]
        p[0] = 1
        p[1] = 1
        
        for i in range(2,n+1):
            for j in range(1,i+1):
                p[i] += p[j-1] * p[i-j]
        return p[n]
