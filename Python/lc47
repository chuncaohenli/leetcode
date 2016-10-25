# DFS
# duplicates element only appear once in each level,
# in other words, duplicates appear once in each position
# so use a set to check whether current ele is duplicate

class Solution(object):
    def recursive(self, permutation, nums,length):
        if len(permutation) == length:
            self.result.append(permutation)
            return
        head = set()

        for i in range(len(nums)):
            tmp_nums = nums[:]
            if not nums[i] in head:
                new_permutation = permutation + [nums[i]]
                head.add(nums[i])
                tmp_nums.remove(nums[i])
                self.recursive(new_permutation, tmp_nums,length)


    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        head = set()
        self.result = []
        permutation = []

        for i in range(len(nums)):
            tmp_nums = nums[:]
            if not nums[i] in head:
                new_permutation = permutation + [nums[i]]
                head.add(nums[i])
                tmp_nums.remove(nums[i])
                self.recursive(new_permutation, tmp_nums,len(nums))


        return self.result
