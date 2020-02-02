s = 'aab'

dp = [i for i in range(len(s))]

for mid in range(len(s)):
    # odd
    l, r = mid, mid
    while l >= 0 and r < len(s) and s[l] == s[r]:
        dp[r] = 0 if l == 0 else min(dp[r], dp[l - 1] + 1)
        l -= 1
        r += 1
    # even
    if mid < len(s) - 1:
        l, r = mid, mid + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            dp[r] = 0 if l == 0 else min(dp[r], dp[l - 1] + 1)
            l -= 1
            r += 1

print(dp)