class Solution {
    public int solution(int num1, int num2) {
        double d1 = Double.valueOf(num1);
        double d2 = Double.valueOf(num2);
        int answer = (int) (d1 / d2 * 1000);
        return answer;
    }
}