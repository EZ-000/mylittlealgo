class Solution {
    public int solution(int n) {
        int n1 = n;
        int n2 = 6;
        
        if (n1 < 6) {
            n2 = n1;
            n1 = 6;
        }
        
        int gcd = getGCD(n1, n2);
        
        int answer = n / gcd;
        return answer;
    }
    
    public static int getGCD(int n, int m) {
        if (n % m == 0) {
            return m;
        }
        return getGCD(m, n % m);
    }
}