# DP
# find every consecutive arithmetic seq and accumulate the result 
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        
        result = 0
        i=0
        
        while i<len(A)-2:
            right = i+2

            while right < len(A) and A[right]-A[right-1] == A[i+1]-A[i]:
                right += 1
            result += sum(range(1,right-1-i))
            
            i = right-1
                

        return result
                    
