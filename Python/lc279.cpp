// have no idea why python version will cause TLE
class Solution {
public:
    int numSquares(int n) {
        int* dp = new int[n+1];
        dp[0] = 0;
        dp[1] = 1;
        
        for (int i=2;i<n+1;i++){
            int j = 1;
            dp[i] = i;
            
            while (j*j<=i){
                int rest = i-j*j;
                if(dp[i] > dp[rest]+1)
                    dp[i] = dp[rest]+1;
                j++;

            }
                
        }
        
        cout << dp[12];
        
        return dp[n];
    }
};
