class Solution {
    public int solution(int n) {
        int answer = 2;
        double s = Math.sqrt(n);
        if (s % 1 == 0) answer = 1;
        return answer;
    }
}