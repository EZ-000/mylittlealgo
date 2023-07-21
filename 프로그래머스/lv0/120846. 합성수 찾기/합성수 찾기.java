import java.lang.Math;

class Solution {
    public int solution(int n) {
        boolean[] visited = new boolean[n];
        int answer = 0;
        for (int number = 2; number < n + 1; number++) {
            for (int multiple = 2 * number; multiple < n + 1; multiple += number) {
                if (!visited[multiple - 1]) {
                    visited[multiple - 1] = true;
                    answer++;
                }
            }
        }
        return answer;
    }
}