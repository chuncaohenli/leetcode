# DP
# 2D
# 0 | 1 2 3 4
#-------------
# 1 | 0 1 2 4
# 2 | 0 0 2 3
# 3 | 0 0 0 3
# 4 | 0 0 0 0
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """

        money = [[0] * (n + 2) for i in range(n + 2)]

        for i in range(1, n + 1):
            money[i][i] = 0
        for i in range(1, n):
            money[i][i + 1] = i

        for length in range(2, n):
            for j in range(1, n + 1 - length):
                minMoney = sys.maxint
                for middle in range(j,j+length+1):
                    middle_money = middle
                    left_money = money[j][middle - 1]
                    right_money = money[middle + 1][j + length]
                    tmp = max(left_money, right_money)
                    minMoney = min(tmp+middle_money, minMoney)
                money[j][j+length] = minMoney


        return money[1][n]
