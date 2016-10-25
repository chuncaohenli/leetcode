# DP
# pay attention to 0,  '0xxxxxxxxxxx' returns 0,   '10'  returns 1
#
#     P(i) = P(i+1) + P(i+2), if int(i,i+1) <= 26
#            P(i+1), else

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0
        if len(s) == 1:
            if s=='0':
                return 0
            return 1
        num_path = []
        for i in range(len(s)):
            if s[i] == '0':
                num_path.append(0)
            else:
                num_path.append(1)
        num_path.append(1)
        
        for i in range(len(s)-1):
            left = int(s[-i-2])
            right = int(s[-i-1])
            
            if left==0:
                continue
            
            if left*10+right <= 26:
                num_path[-i-3] = num_path[-i-1] + num_path[-i-2]
            else:
                num_path[-i-3] = num_path[-i-2]
        return num_path[0]
