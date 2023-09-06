import java.math.BigInteger;

class Solution {
    public int solution(int n) {
        BigInteger[] fibonacci = new BigInteger[n + 1];
        fibonacci[0] = BigInteger.ZERO;
        fibonacci[1] = BigInteger.ONE;

        for (int index = 2; index <= n; index++) {
            fibonacci[index] = fibonacci[index - 2].add(fibonacci[index - 1]);
        }

        return fibonacci[n].mod(BigInteger.valueOf(1234567)).intValue();
    }
}