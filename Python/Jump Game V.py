class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        s_arr = []
        for i, a in enumerate(arr):
            s_arr.append((a, i))
        s_arr.sort()

        dp = [1] * len(arr)

        for a, i in s_arr:
            # to left
            j = 1
            l_max = arr[i]
            for j in range(1, d + 1):
                if i - j >= 0:
                    if arr[i - j] <= arr[i]:
                        continue
                    else:
                        if arr[i - j] > l_max:
                            dp[i - j] = max(dp[i - j], dp[i] + 1)
                            l_max = arr[i - j]
                        else:
                            break
                else:
                    break
            # to right
            j = 1
            r_max = arr[i]
            for j in range(1, d + 1):
                if i + j < len(arr):
                    if arr[i + j] <= arr[i]:
                        continue
                    else:
                        if arr[i + j] > r_max:
                            r_max = arr[i + j]
                            dp[i + j] = max(dp[i + j], dp[i] + 1)
                        else:
                            break
                else:
                    break
        return max(dp)