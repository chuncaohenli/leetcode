# DP
# Use set to reduce space complexity

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) / 2
        
        sum_set = set()
        
        for num in nums:
            
            if num == target:
                return True
            tmp = set()
            for ss in sum_set:
                new = ss + num
                
                if new > target:
                    continue
                
                if new == target:
                    return True
                    
                tmp.add(new)
            for tt in tmp:
                sum_set.add(tt)
            sum_set.add(num)
        
        
        return False
