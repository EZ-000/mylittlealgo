class Solution {
    public int solution(int n) {
        int answer = 0;
        int reversedFactorial = 1;
        while (true) {
            answer++;
            reversedFactorial *= answer;
            if (n <= reversedFactorial) {
                answer = (n < reversedFactorial) ? answer - 1 : answer;
                break;
            }
        }
        return answer;
    }
}