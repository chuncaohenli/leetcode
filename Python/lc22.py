class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                for x in dp[j]:
                    for y in dp[i - j - 1]:
                        dp[i].append('(' + x + ')' + y )
        return dp[n]

s = Solution()
for i in range(10):
    r = s.generateParenthesis(i)
    print(len(r), r)