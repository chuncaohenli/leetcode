class Solution:
    # TLE
    def subarraySum(self, nums, k):
        pre_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        res = 0
        for r in range(1, len(nums) + 1):
            for l in range(r):
                if k == pre_sum[r] - pre_sum[l]:
                    res += 1
        return res

    def subarraySum2(self, nums, k):
        pre_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        res = 0
        mem = set()
        for p in pre_sum:
            if p - k in mem:
                res += 1
            mem.add(p)
        return res

    def subarraySum3(self, nums, k) -> int:
        import collections
        mem = collections.defaultdict(int)
        mem[0] = 1
        pre_sum = 0
        res = 0
        for num in nums:
            pre_sum += num
            res += mem[pre_sum - k]
            mem[pre_sum] += 1
        return res

s = Solution()
#print(s.subarraySum([1,2,3],3))
#print(s.subarraySum2([1,2,3],3))
print(s.subarraySum3([1,2,3],3))