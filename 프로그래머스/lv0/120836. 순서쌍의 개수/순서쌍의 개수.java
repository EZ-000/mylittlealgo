class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int d = 1; d <= n; d++) {
            if (n % d == 0) {
                answer += 1;
            }
        }
        return answer;
    }
}