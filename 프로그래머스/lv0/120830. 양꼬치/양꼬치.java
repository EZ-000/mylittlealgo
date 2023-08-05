class Solution {
    public int solution(int n, int k) {
        if (10 <= n) {
            k -= n / 10;
        }
        return 12000 * n + 2000 * k;
    }
}