class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int numer3 = numer1 * denom2 + numer2 * denom1;
        int denom3 = denom1 * denom2;
        
        int gcd = getGCD(numer3, denom3);
        
        int[] answer = {numer3 / gcd, denom3 / gcd};
        
        return answer;
    }
    
    public static int getGCD(int n1, int n2) {
        if (n1 % n2 == 0) {
            return n2;
        }
        return getGCD(n2, n1 % n2);
    }
}