import java.math.BigInteger;

class Solution {
    private BigInteger getFactorialWithEnd(int start, int end) {
        BigInteger result = new BigInteger("1");
        for (int n = start; n <= end; n++) {
            BigInteger bigInteger = new BigInteger(n + "");
            result = result.multiply(bigInteger);
        }
        return result;
    }
    
    private int combination(int n, int m) {
        int r = n - m;
        int denominator1 = (r < m) ? m : r;
        int denominator2 = (r < m) ? r : m;
        
        BigInteger result = getFactorialWithEnd(denominator1 + 1, n).divide(getFactorialWithEnd(1, denominator2));
        
        return result.intValue();
    }
    
    public int solution(int balls, int share) {
        return combination(balls, share);
    }
}