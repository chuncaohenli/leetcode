class Solution:
    def minCostII(self, costs):
        if not costs:
            return 0
        n, k = len(costs), len(costs[0])
        min1, min2 = -1, -1
        for i, colors in enumerate(costs):
            cur_min1, cur_min2 = -1, -1
            for j, c in enumerate(colors):
                # update cur dp val
                if i > 0:
                    print(min1, min2)
                    if min1 == j:
                        costs[i][j] = c + costs[i-1][min2]
                    else:
                        costs[i][j] = c + costs[i-1][min1]
                # update min1
                if cur_min1 == -1 or costs[i][j] < colors[cur_min1]:
                    cur_min2 = cur_min1
                    cur_min1 = j
                # update min2
                elif cur_min2 == -1 or costs[i][j] < colors[cur_min2]:
                    cur_min2 = j
            min1, min2 = cur_min1, cur_min2

        return costs[-1][min1]

s = Solution()
#costs = [[1,5,3],[2,9,4]]
costs = [[20,19,11,13,12,16,16,17,15,9,5,18],[3,8,15,17,19,8,18,3,11,6,7,12],[15,4,11,1,18,2,10,9,3,6,4,15]]
s.minCostII(costs)