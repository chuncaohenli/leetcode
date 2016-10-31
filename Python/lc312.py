# Always know the situation of last shoot
# DP 
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [1] + nums + [1]
        mem = [[0] * len(nums) for num in nums]

        for length in range(1, n + 1):
            for left in range(1, n + 2 - length):
                right = left + length - 1
                for i in range(left,right+1):
                    lastShoot = nums[left-1] * nums[right+1] * nums[i]
                    #important
                    mem[left][right] = max(mem[left][right],lastShoot+mem[left][i-1]+mem[i+1][right])

        return mem[1][n]
