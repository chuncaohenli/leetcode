# 1-d DP is enough, boy
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.array = [nums[i] for i in range(len(nums))]
        
        for i in range(1,len(nums)):
            self.array[i] += self.array[i-1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==0:
            return self.array[j]
        else:
            return self.array[j] - self.array[i-1]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
