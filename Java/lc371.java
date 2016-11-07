// calculate carry first by &
// calculate result without considering the carry by ^

public class Solution {
    public int getSum(int a, int b) {
        while (b!=0){
            int carry = a&b;
            a = a^b;
            b = carry << 1;
        }
        return a;
    }
}
