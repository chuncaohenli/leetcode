# if there is no negative number, product all
# local_min(i) == total_min(i)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_min = local_max = total_max = nums[0]
        
        for i in range(1,len(nums)):
            tmp_min = nums[i] * total_min
            tmp_max = nums[i] * local_max
            total_min = min(min(tmp_min,tmp_max),nums[i])
            local_max = max(max(tmp_max,tmp_min),nums[i])
            total_max = max(total_max,local_max)
        return total_max
