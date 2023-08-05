class Solution {
    private int getGCD(int n1, int n2) {
        if (n1 % n2 == 0) return n2;
        return getGCD(n2, n1 % n2);
    }
    
    public int solution(int a, int b) {
        int gcd = getGCD(a, b);
        
        a /= gcd;
        b /= gcd;
        
        while (b % 2 == 0) b /= 2;
        while (b % 5 == 0) b /= 5;
        
        return (b == 1) ? 1 : 2;
    }
}